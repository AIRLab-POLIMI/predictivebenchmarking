// Auto-generated. Do not edit!

// (in-package adhoc_communication.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let CMgrRobotUpdate = require('../msg/CMgrRobotUpdate.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SendCMgrRobotUpdateRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.dst_robot = null;
      this.topic = null;
      this.update = null;
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
      if (initObj.hasOwnProperty('update')) {
        this.update = initObj.update
      }
      else {
        this.update = new CMgrRobotUpdate();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SendCMgrRobotUpdateRequest
    // Serialize message field [dst_robot]
    bufferOffset = _serializer.string(obj.dst_robot, buffer, bufferOffset);
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [update]
    bufferOffset = CMgrRobotUpdate.serialize(obj.update, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendCMgrRobotUpdateRequest
    let len;
    let data = new SendCMgrRobotUpdateRequest(null);
    // Deserialize message field [dst_robot]
    data.dst_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [update]
    data.update = CMgrRobotUpdate.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.dst_robot.length;
    length += object.topic.length;
    length += CMgrRobotUpdate.getMessageSize(object.update);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendCMgrRobotUpdateRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bd04cde8f0ddfa8f82410ab8a1e2aa20';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string dst_robot
    string topic
    adhoc_communication/CMgrRobotUpdate update
    
    ================================================================================
    MSG: adhoc_communication/CMgrRobotUpdate
    string robot_name
    string capabilities
    float32 energy
    adhoc_communication/CMgrDimensions dimensions
    string status
    string[] neighbors
    
    ================================================================================
    MSG: adhoc_communication/CMgrDimensions
    float32 x
    float32 y
    float32 z
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SendCMgrRobotUpdateRequest(null);
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

    if (msg.update !== undefined) {
      resolved.update = CMgrRobotUpdate.Resolve(msg.update)
    }
    else {
      resolved.update = new CMgrRobotUpdate()
    }

    return resolved;
    }
};

class SendCMgrRobotUpdateResponse {
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
    // Serializes a message object of type SendCMgrRobotUpdateResponse
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendCMgrRobotUpdateResponse
    let len;
    let data = new SendCMgrRobotUpdateResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendCMgrRobotUpdateResponse';
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
    const resolved = new SendCMgrRobotUpdateResponse(null);
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
  Request: SendCMgrRobotUpdateRequest,
  Response: SendCMgrRobotUpdateResponse,
  md5sum() { return '2ccd371ff7aeb961749b74bac24a3996'; },
  datatype() { return 'adhoc_communication/SendCMgrRobotUpdate'; }
};
