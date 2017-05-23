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

class RecvString {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.src_robot = null;
      this.data = null;
    }
    else {
      if (initObj.hasOwnProperty('src_robot')) {
        this.src_robot = initObj.src_robot
      }
      else {
        this.src_robot = '';
      }
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RecvString
    // Serialize message field [src_robot]
    bufferOffset = _serializer.string(obj.src_robot, buffer, bufferOffset);
    // Serialize message field [data]
    bufferOffset = _serializer.string(obj.data, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RecvString
    let len;
    let data = new RecvString(null);
    // Deserialize message field [src_robot]
    data.src_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [data]
    data.data = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.src_robot.length;
    length += object.data.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/RecvString';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '357efa7118aea6ce32be041203afb4ca';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string src_robot
    string data
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RecvString(null);
    if (msg.src_robot !== undefined) {
      resolved.src_robot = msg.src_robot;
    }
    else {
      resolved.src_robot = ''
    }

    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = ''
    }

    return resolved;
    }
};

module.exports = RecvString;
