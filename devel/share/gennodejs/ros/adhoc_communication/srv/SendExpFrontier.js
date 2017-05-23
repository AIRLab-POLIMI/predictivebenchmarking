// Auto-generated. Do not edit!

// (in-package adhoc_communication.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ExpFrontier = require('../msg/ExpFrontier.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SendExpFrontierRequest {
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
        this.frontier = new ExpFrontier();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SendExpFrontierRequest
    // Serialize message field [dst_robot]
    bufferOffset = _serializer.string(obj.dst_robot, buffer, bufferOffset);
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [frontier]
    bufferOffset = ExpFrontier.serialize(obj.frontier, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendExpFrontierRequest
    let len;
    let data = new SendExpFrontierRequest(null);
    // Deserialize message field [dst_robot]
    data.dst_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [frontier]
    data.frontier = ExpFrontier.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.dst_robot.length;
    length += object.topic.length;
    length += ExpFrontier.getMessageSize(object.frontier);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendExpFrontierRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'da93ebf66d2d90a5278c997ea3c0023b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string dst_robot
    string topic
    adhoc_communication/ExpFrontier frontier
    
    ================================================================================
    MSG: adhoc_communication/ExpFrontier
    ExpFrontierElement[] frontier_element
    
    ================================================================================
    MSG: adhoc_communication/ExpFrontierElement
    int64 id
    string detected_by_robot_str
    int64 detected_by_robot
    float64 robot_home_position_x
    float64 robot_home_position_y
    float64 x_coordinate
    float64 y_coordinate
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SendExpFrontierRequest(null);
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
      resolved.frontier = ExpFrontier.Resolve(msg.frontier)
    }
    else {
      resolved.frontier = new ExpFrontier()
    }

    return resolved;
    }
};

class SendExpFrontierResponse {
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
    // Serializes a message object of type SendExpFrontierResponse
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendExpFrontierResponse
    let len;
    let data = new SendExpFrontierResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendExpFrontierResponse';
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
    const resolved = new SendExpFrontierResponse(null);
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
  Request: SendExpFrontierRequest,
  Response: SendExpFrontierResponse,
  md5sum() { return 'd7217cbccb23cf4e4e1279a92f585b8a'; },
  datatype() { return 'adhoc_communication/SendExpFrontier'; }
};
