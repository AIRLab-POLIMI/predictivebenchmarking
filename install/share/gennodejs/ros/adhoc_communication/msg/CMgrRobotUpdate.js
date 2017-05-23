// Auto-generated. Do not edit!

// (in-package adhoc_communication.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let CMgrDimensions = require('./CMgrDimensions.js');

//-----------------------------------------------------------

class CMgrRobotUpdate {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.robot_name = null;
      this.capabilities = null;
      this.energy = null;
      this.dimensions = null;
      this.status = null;
      this.neighbors = null;
    }
    else {
      if (initObj.hasOwnProperty('robot_name')) {
        this.robot_name = initObj.robot_name
      }
      else {
        this.robot_name = '';
      }
      if (initObj.hasOwnProperty('capabilities')) {
        this.capabilities = initObj.capabilities
      }
      else {
        this.capabilities = '';
      }
      if (initObj.hasOwnProperty('energy')) {
        this.energy = initObj.energy
      }
      else {
        this.energy = 0.0;
      }
      if (initObj.hasOwnProperty('dimensions')) {
        this.dimensions = initObj.dimensions
      }
      else {
        this.dimensions = new CMgrDimensions();
      }
      if (initObj.hasOwnProperty('status')) {
        this.status = initObj.status
      }
      else {
        this.status = '';
      }
      if (initObj.hasOwnProperty('neighbors')) {
        this.neighbors = initObj.neighbors
      }
      else {
        this.neighbors = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CMgrRobotUpdate
    // Serialize message field [robot_name]
    bufferOffset = _serializer.string(obj.robot_name, buffer, bufferOffset);
    // Serialize message field [capabilities]
    bufferOffset = _serializer.string(obj.capabilities, buffer, bufferOffset);
    // Serialize message field [energy]
    bufferOffset = _serializer.float32(obj.energy, buffer, bufferOffset);
    // Serialize message field [dimensions]
    bufferOffset = CMgrDimensions.serialize(obj.dimensions, buffer, bufferOffset);
    // Serialize message field [status]
    bufferOffset = _serializer.string(obj.status, buffer, bufferOffset);
    // Serialize message field [neighbors]
    bufferOffset = _arraySerializer.string(obj.neighbors, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CMgrRobotUpdate
    let len;
    let data = new CMgrRobotUpdate(null);
    // Deserialize message field [robot_name]
    data.robot_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [capabilities]
    data.capabilities = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [energy]
    data.energy = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [dimensions]
    data.dimensions = CMgrDimensions.deserialize(buffer, bufferOffset);
    // Deserialize message field [status]
    data.status = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [neighbors]
    data.neighbors = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.robot_name.length;
    length += object.capabilities.length;
    length += object.status.length;
    object.neighbors.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/CMgrRobotUpdate';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '624d872396e6c4effefdaa51af9e8904';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new CMgrRobotUpdate(null);
    if (msg.robot_name !== undefined) {
      resolved.robot_name = msg.robot_name;
    }
    else {
      resolved.robot_name = ''
    }

    if (msg.capabilities !== undefined) {
      resolved.capabilities = msg.capabilities;
    }
    else {
      resolved.capabilities = ''
    }

    if (msg.energy !== undefined) {
      resolved.energy = msg.energy;
    }
    else {
      resolved.energy = 0.0
    }

    if (msg.dimensions !== undefined) {
      resolved.dimensions = CMgrDimensions.Resolve(msg.dimensions)
    }
    else {
      resolved.dimensions = new CMgrDimensions()
    }

    if (msg.status !== undefined) {
      resolved.status = msg.status;
    }
    else {
      resolved.status = ''
    }

    if (msg.neighbors !== undefined) {
      resolved.neighbors = msg.neighbors;
    }
    else {
      resolved.neighbors = []
    }

    return resolved;
    }
};

module.exports = CMgrRobotUpdate;
