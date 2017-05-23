// Auto-generated. Do not edit!

// (in-package adhoc_communication.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let EmDockingStation = require('../msg/EmDockingStation.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SendEmDockingStationRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.topic = null;
      this.dst_robot = null;
      this.docking_station = null;
    }
    else {
      if (initObj.hasOwnProperty('topic')) {
        this.topic = initObj.topic
      }
      else {
        this.topic = '';
      }
      if (initObj.hasOwnProperty('dst_robot')) {
        this.dst_robot = initObj.dst_robot
      }
      else {
        this.dst_robot = '';
      }
      if (initObj.hasOwnProperty('docking_station')) {
        this.docking_station = initObj.docking_station
      }
      else {
        this.docking_station = new EmDockingStation();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SendEmDockingStationRequest
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [dst_robot]
    bufferOffset = _serializer.string(obj.dst_robot, buffer, bufferOffset);
    // Serialize message field [docking_station]
    bufferOffset = EmDockingStation.serialize(obj.docking_station, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendEmDockingStationRequest
    let len;
    let data = new SendEmDockingStationRequest(null);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [dst_robot]
    data.dst_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [docking_station]
    data.docking_station = EmDockingStation.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.topic.length;
    length += object.dst_robot.length;
    return length + 29;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendEmDockingStationRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2f280699aa71232ca76f0fe6d48ebf33';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string topic
    string dst_robot
    adhoc_communication/EmDockingStation docking_station
    
    ================================================================================
    MSG: adhoc_communication/EmDockingStation
    int32 id
    float64 x
    float64 y
    bool vacant
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SendEmDockingStationRequest(null);
    if (msg.topic !== undefined) {
      resolved.topic = msg.topic;
    }
    else {
      resolved.topic = ''
    }

    if (msg.dst_robot !== undefined) {
      resolved.dst_robot = msg.dst_robot;
    }
    else {
      resolved.dst_robot = ''
    }

    if (msg.docking_station !== undefined) {
      resolved.docking_station = EmDockingStation.Resolve(msg.docking_station)
    }
    else {
      resolved.docking_station = new EmDockingStation()
    }

    return resolved;
    }
};

class SendEmDockingStationResponse {
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
    // Serializes a message object of type SendEmDockingStationResponse
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendEmDockingStationResponse
    let len;
    let data = new SendEmDockingStationResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendEmDockingStationResponse';
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
    const resolved = new SendEmDockingStationResponse(null);
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
  Request: SendEmDockingStationRequest,
  Response: SendEmDockingStationResponse,
  md5sum() { return '8f86c3f7e9c77062fc3c620d3c267397'; },
  datatype() { return 'adhoc_communication/SendEmDockingStation'; }
};
