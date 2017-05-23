// Auto-generated. Do not edit!

// (in-package adhoc_communication.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let MmPoint = require('../msg/MmPoint.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SendMmPointRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.dst_robot = null;
      this.topic = null;
      this.point = null;
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
      if (initObj.hasOwnProperty('point')) {
        this.point = initObj.point
      }
      else {
        this.point = new MmPoint();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SendMmPointRequest
    // Serialize message field [dst_robot]
    bufferOffset = _serializer.string(obj.dst_robot, buffer, bufferOffset);
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [point]
    bufferOffset = MmPoint.serialize(obj.point, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendMmPointRequest
    let len;
    let data = new SendMmPointRequest(null);
    // Deserialize message field [dst_robot]
    data.dst_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [point]
    data.point = MmPoint.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.dst_robot.length;
    length += object.topic.length;
    length += MmPoint.getMessageSize(object.point);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendMmPointRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '804c836a23c6b90c2c1269b2dff70c05';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string dst_robot
    string topic
    adhoc_communication/MmPoint point
    
    ================================================================================
    MSG: adhoc_communication/MmPoint
    string src_robot
    float64 x
    float64 y
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SendMmPointRequest(null);
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

    if (msg.point !== undefined) {
      resolved.point = MmPoint.Resolve(msg.point)
    }
    else {
      resolved.point = new MmPoint()
    }

    return resolved;
    }
};

class SendMmPointResponse {
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
    // Serializes a message object of type SendMmPointResponse
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendMmPointResponse
    let len;
    let data = new SendMmPointResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendMmPointResponse';
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
    const resolved = new SendMmPointResponse(null);
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
  Request: SendMmPointRequest,
  Response: SendMmPointResponse,
  md5sum() { return 'caf6ffd259d365577a9cd46d32b9cb17'; },
  datatype() { return 'adhoc_communication/SendMmPoint'; }
};
