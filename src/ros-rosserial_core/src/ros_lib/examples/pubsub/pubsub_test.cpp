#include <stdlib.h> // atof()

#include "ch.h"
#include "hal.h"
#include "usbcfg.h"

#define USE_USB_SERIAL 1

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Empty.h>

#if USE_USB_SERIAL
#define usb_lld_connect_bus(usbp)
#define usb_lld_disconnect_bus(usbp)
#endif

/*
 * ROS node.
 */

ros::NodeHandle nh;


/*
 * ROS rosserial publisher thread.
 */
msg_t rosserial_pub_thread(void * arg) {
	std_msgs::String str_msg;
	ros::Publisher pub("chatter", &str_msg);

	(void) arg;
	chRegSetThreadName("rosserial_pub");

	nh.initNode();
	nh.advertise(pub);

	for (;;) {
		char hello[] = "Hello world!";
		str_msg.data = hello;
		pub.publish(&str_msg);
		nh.spinOnce();
		chThdSleepMilliseconds(500);
	}

	return CH_SUCCESS;
}


/*
 * ROS rosserial subscriber thread.
 */

void msg_cb( const std_msgs::Empty& toggle_msg){
	palTogglePad(LED1_GPIO, LED1);
}

msg_t rosserial_sub_thread(void * arg) {
	ros::Subscriber<std_msgs::Empty> sub("toggle_led", &msg_cb );

	(void) arg;
	chRegSetThreadName("rosserial_sub");

	nh.initNode();
	nh.subscribe(sub);

	for (;;) {
		nh.spinOnce();
		chThdSleepMilliseconds(5);
	}

	return CH_SUCCESS;
}


/*
 * Application entry point.
 */
extern "C" {
int main(void) {
	Thread * pub_tp = NULL;
	Thread * sub_tp = NULL;

	halInit();
	chSysInit();

	/*
	 * Initializes a serial-over-USB CDC driver.
	 */
#if USE_USB_SERIAL
	sduObjectInit(&SDU1);
	sduStart(&SDU1, &serusbcfg);
#endif

	/*
	 * Activates the USB driver and then the USB bus pull-up on D+.
	 * Note, a delay is inserted in order to not have to disconnect the cable
	 * after a reset.
	 */
#if USE_USB_SERIAL
	usbDisconnectBus(serusbcfg.usbp);
	chThdSleepMilliseconds(500);
	usbStart(serusbcfg.usbp, &usbcfg);
	usbConnectBus(serusbcfg.usbp);
#endif

	/* Start the serial driver. */
#if !USE_USB_SERIAL
	sdStart(&SD3, NULL);
#endif

	for (;;) {
#if USE_USB_SERIAL
		if (!pub_tp && (SDU1.config->usbp->state == USB_ACTIVE)) {
#else
		if (!pub_tp) {
#endif
			pub_tp = chThdCreateFromHeap(NULL, THD_WA_SIZE(2048), NORMALPRIO, rosserial_pub_thread, NULL);
		} else if (chThdTerminated(pub_tp)) {
			chThdRelease(pub_tp);
			pub_tp = NULL;
		}

		chThdSleepMilliseconds(123);

#if USE_USB_SERIAL
		if (!sub_tp && (SDU1.config->usbp->state == USB_ACTIVE)) {
#else
		if (!sub_tp) {
#endif
			sub_tp = chThdCreateFromHeap(NULL, THD_WA_SIZE(2048), NORMALPRIO, rosserial_sub_thread, NULL);
		} else if (chThdTerminated(sub_tp)) {
			chThdRelease(sub_tp);
			sub_tp = NULL;
		}

		chThdSleepMilliseconds(500);
	}

	return CH_SUCCESS;
}
}

