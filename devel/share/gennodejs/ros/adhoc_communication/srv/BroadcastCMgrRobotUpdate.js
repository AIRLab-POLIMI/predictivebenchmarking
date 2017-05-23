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

class BroadcastCMgrRobotUpdateRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.topic = null;
      this.update = null;
      this.hop_limit = null;
    }
    else {
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
      if (initObj.hasOwnProperty('hop_limit')) {
        this.hop_limit = initObj.hop_limit
      }
      else {
        this.hop_limit = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type BroadcastCMgrRobotUpdateRequest
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [update]
    bufferOffset = CMgrRobotUpdate.serialize(obj.update, buffer, bufferOffset);
    // Serialize message field [hop_limit]
    bufferOffset = _serializer.uint8(obj.hop_limit, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BroadcastCMgrRobotUpdateRequest
    let len;
    let data = new BroadcastCMgrRobotUpdateRequest(null);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [update]
    data.update = CMgrRobotUpdate.deserialize(buffer, bufferOffset);
    // Deserialize message field [hop_limit]
    data.hop_limit = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.topic.length;
    length += CMgrRobotUpdate.getMessageSize(object.update);
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/BroadcastCMgrRobotUpdateRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3bebbc6c00d47ea04f96af1cfc986a55';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string topic
    adhoc_communication/CMgrRobotUpdate update
    uint8 hop_limit
    
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
    const resolved = new BroadcastCMgrRobotUpdateRequest(null);
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

    if (msg.hop_limit !== undefined) {
      resolved.hop_limit = msg.hop_limit;
    }
    else {
      resolved.hop_limit = 0
    }

    return resolved;
    }
};

class BroadcastCMgrRobotUpdateResponse {
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
    // Serializes a message object of type BroadcastCMgrRobotUpdateResponse
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BroadcastCMgrRobotUpdateResponse
    let len;
    let data = new BroadcastCMgrRobotUpdateResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/BroadcastCMgrRobotUpdateResponse';
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
    const resolved = new BroadcastCMgrRobotUpdateResponse(null);
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
  Request: BroadcastCMgrRobotUpdateRequest,
  Response: BroadcastCMgrRobotUpdateResponse,
  md5sum() { return '4f803d834e6e3f0165ecc26babd1f3f1'; },
  datatype() { return 'adhoc_communication/BroadcastCMgrRobotUpdate'; }
};
