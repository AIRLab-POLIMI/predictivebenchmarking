// Generated by gencpp from file adhoc_communication/SendMmRobotPositionRequest.msg
// DO NOT EDIT!


#ifndef ADHOC_COMMUNICATION_MESSAGE_SENDMMROBOTPOSITIONREQUEST_H
#define ADHOC_COMMUNICATION_MESSAGE_SENDMMROBOTPOSITIONREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <adhoc_communication/MmRobotPosition.h>

namespace adhoc_communication
{
template <class ContainerAllocator>
struct SendMmRobotPositionRequest_
{
  typedef SendMmRobotPositionRequest_<ContainerAllocator> Type;

  SendMmRobotPositionRequest_()
    : dst_robot()
    , topic()
    , position()  {
    }
  SendMmRobotPositionRequest_(const ContainerAllocator& _alloc)
    : dst_robot(_alloc)
    , topic(_alloc)
    , position(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _dst_robot_type;
  _dst_robot_type dst_robot;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _topic_type;
  _topic_type topic;

   typedef  ::adhoc_communication::MmRobotPosition_<ContainerAllocator>  _position_type;
  _position_type position;




  typedef boost::shared_ptr< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SendMmRobotPositionRequest_

typedef ::adhoc_communication::SendMmRobotPositionRequest_<std::allocator<void> > SendMmRobotPositionRequest;

typedef boost::shared_ptr< ::adhoc_communication::SendMmRobotPositionRequest > SendMmRobotPositionRequestPtr;
typedef boost::shared_ptr< ::adhoc_communication::SendMmRobotPositionRequest const> SendMmRobotPositionRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace adhoc_communication

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'adhoc_communication': ['/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "58e53492a8835f0741305155e91765cb";
  }

  static const char* value(const ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x58e53492a8835f07ULL;
  static const uint64_t static_value2 = 0x41305155e91765cbULL;
};

template<class ContainerAllocator>
struct DataType< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "adhoc_communication/SendMmRobotPositionRequest";
  }

  static const char* value(const ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string dst_robot\n\
string topic\n\
adhoc_communication/MmRobotPosition position\n\
\n\
================================================================================\n\
MSG: adhoc_communication/MmRobotPosition\n\
string src_robot\n\
geometry_msgs/PoseStamped position\n\
\n\
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of position and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
";
  }

  static const char* value(const ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.dst_robot);
      stream.next(m.topic);
      stream.next(m.position);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SendMmRobotPositionRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::adhoc_communication::SendMmRobotPositionRequest_<ContainerAllocator>& v)
  {
    s << indent << "dst_robot: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.dst_robot);
    s << indent << "topic: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.topic);
    s << indent << "position: ";
    s << std::endl;
    Printer< ::adhoc_communication::MmRobotPosition_<ContainerAllocator> >::stream(s, indent + "  ", v.position);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ADHOC_COMMUNICATION_MESSAGE_SENDMMROBOTPOSITIONREQUEST_H
