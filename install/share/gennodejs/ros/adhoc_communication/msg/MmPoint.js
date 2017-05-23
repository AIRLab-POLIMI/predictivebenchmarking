// Auto-generated. Do not edit!

// (in-package adhoc_communication.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class MmPoint {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.src_robot = null;
      this.x = null;
      this.y = null;
    }
    else {
      if (initObj.hasOwnProperty('src_robot')) {
        this.src_robot = initObj.src_robot
      }
      else {
        this.src_robot = '';
      }
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0.0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MmPoint
    // Serialize message field [src_robot]
    bufferOffset = _serializer.string(obj.src_robot, buffer, bufferOffset);
    // Serialize message field [x]
    bufferOffset = _serializer.float64(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.float64(obj.y, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MmPoint
    let len;
    let data = new MmPoint(null);
    // Deserialize message field [src_robot]
    data.src_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [x]
    data.x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.src_robot.length;
    return length + 20;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/MmPoint';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bf827d01cbf6a28b70ad364cdc656d65';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new MmPoint(null);
    if (msg.src_robot !== undefined) {
      resolved.src_robot = msg.src_robot;
    }
    else {
      resolved.src_robot = ''
    }

    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0.0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0.0
    }

    return resolved;
    }
};

module.exports = MmPoint;
