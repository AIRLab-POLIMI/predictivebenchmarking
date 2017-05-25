// Auto-generated. Do not edit!

// (in-package nav2d_operator.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class cmd {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Velocity = null;
      this.Turn = null;
      this.Mode = null;
    }
    else {
      if (initObj.hasOwnProperty('Velocity')) {
        this.Velocity = initObj.Velocity
      }
      else {
        this.Velocity = 0.0;
      }
      if (initObj.hasOwnProperty('Turn')) {
        this.Turn = initObj.Turn
      }
      else {
        this.Turn = 0.0;
      }
      if (initObj.hasOwnProperty('Mode')) {
        this.Mode = initObj.Mode
      }
      else {
        this.Mode = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type cmd
    // Serialize message field [Velocity]
    bufferOffset = _serializer.float64(obj.Velocity, buffer, bufferOffset);
    // Serialize message field [Turn]
    bufferOffset = _serializer.float64(obj.Turn, buffer, bufferOffset);
    // Serialize message field [Mode]
    bufferOffset = _serializer.int8(obj.Mode, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type cmd
    let len;
    let data = new cmd(null);
    // Deserialize message field [Velocity]
    data.Velocity = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Turn]
    data.Turn = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [Mode]
    data.Mode = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 17;
  }

  static datatype() {
    // Returns string type for a message object
    return 'nav2d_operator/cmd';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '90c9a043660646e2102f124332ecb8b7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 Velocity
    float64 Turn
    int8    Mode
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new cmd(null);
    if (msg.Velocity !== undefined) {
      resolved.Velocity = msg.Velocity;
    }
    else {
      resolved.Velocity = 0.0
    }

    if (msg.Turn !== undefined) {
      resolved.Turn = msg.Turn;
    }
    else {
      resolved.Turn = 0.0
    }

    if (msg.Mode !== undefined) {
      resolved.Mode = msg.Mode;
    }
    else {
      resolved.Mode = 0
    }

    return resolved;
    }
};

module.exports = cmd;
