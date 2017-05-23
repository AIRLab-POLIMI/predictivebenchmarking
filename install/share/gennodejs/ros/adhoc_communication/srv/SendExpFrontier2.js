// Auto-generated. Do not edit!

// (in-package adhoc_communication.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ExpFrontierElement = require('../msg/ExpFrontierElement.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SendExpFrontier2Request {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.dst_robot = null;
      this.topic = null;
      this.frontier = null;
    }
    else {
      if (initObj.hasOwnProperty('dst_robot')) {
        this.dst_robot = initObj.dst_robot
      }
      else {
        this.dst_robot = '';
      }
      if (initObj.hasOwnProperty('topic')) {
        this.topic = initObj.topic
      }
      else {
        this.topic = '';
      }
      if (initObj.hasOwnProperty('frontier')) {
        this.frontier = initObj.frontier
      }
      else {
        this.frontier = new ExpFrontierElement();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SendExpFrontier2Request
    // Serialize message field [dst_robot]
    bufferOffset = _serializer.string(obj.dst_robot, buffer, bufferOffset);
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [frontier]
    bufferOffset = ExpFrontierElement.serialize(obj.frontier, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendExpFrontier2Request
    let len;
    let data = new SendExpFrontier2Request(null);
    // Deserialize message field [dst_robot]
    data.dst_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [frontier]
    data.frontier = ExpFrontierElement.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.dst_robot.length;
    length += object.topic.length;
    length += ExpFrontierElement.getMessageSize(object.frontier);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendExpFrontier2Request';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0a5a0643f3b393489d036b9bba8665ac';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string dst_robot
    string topic
    adhoc_communication/ExpFrontierElement frontier
    
    ================================================================================
    MSG: adhoc_communication/ExpFrontierElement
    int64 id
    string detected_by_robot_str
    int64 detected_by_robot
    float64 robot_home_position_x
    float64 robot_home_position_y
    float64 x_coordinate
    float64 y_coordinate
    float64 bid
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SendExpFrontier2Request(null);
    if (msg.dst_robot !== undefined) {
      resolved.dst_robot = msg.dst_robot;
    }
    else {
      resolved.dst_robot = ''
    }

    if (msg.topic !== undefined) {
      resolved.topic = msg.topic;
    }
    else {
      resolved.topic = ''
    }

    if (msg.frontier !== undefined) {
      resolved.frontier = ExpFrontierElement.Resolve(msg.frontier)
    }
    else {
      resolved.frontier = new ExpFrontierElement()
    }

    return resolved;
    }
};

class SendExpFrontier2Response {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.status = null;
    }
    else {
      if (initObj.hasOwnProperty('status')) {
        this.status = initObj.status
      }
      else {
        this.status = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SendExpFrontier2Response
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendExpFrontier2Response
    let len;
    let data = new SendExpFrontier2Response(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendExpFrontier2Response';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '284aa12dd9e9e760802ac9f38036ea5e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 status
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SendExpFrontier2Response(null);
    if (msg.status !== undefined) {
      resolved.status = msg.status;
    }
    else {
      resolved.status = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: SendExpFrontier2Request,
  Response: SendExpFrontier2Response,
  md5sum() { return 'c95ef85b5ba5b536a769a25a3d571277'; },
  datatype() { return 'adhoc_communication/SendExpFrontier2'; }
};
