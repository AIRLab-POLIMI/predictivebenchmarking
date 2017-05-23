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

class MmControl {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.src_robot = null;
      this.update_numbers = null;
    }
    else {
      if (initObj.hasOwnProperty('src_robot')) {
        this.src_robot = initObj.src_robot
      }
      else {
        this.src_robot = '';
      }
      if (initObj.hasOwnProperty('update_numbers')) {
        this.update_numbers = initObj.update_numbers
      }
      else {
        this.update_numbers = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type MmControl
    // Serialize message field [src_robot]
    bufferOffset = _serializer.string(obj.src_robot, buffer, bufferOffset);
    // Serialize message field [update_numbers]
    bufferOffset = _arraySerializer.int32(obj.update_numbers, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type MmControl
    let len;
    let data = new MmControl(null);
    // Deserialize message field [src_robot]
    data.src_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [update_numbers]
    data.update_numbers = _arrayDeserializer.int32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.src_robot.length;
    length += 4 * object.update_numbers.length;
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/MmControl';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3d223057e1839a50fdaaef262568a5a7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string src_robot
    int32[] update_numbers
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new MmControl(null);
    if (msg.src_robot !== undefined) {
      resolved.src_robot = msg.src_robot;
    }
    else {
      resolved.src_robot = ''
    }

    if (msg.update_numbers !== undefined) {
      resolved.update_numbers = msg.update_numbers;
    }
    else {
      resolved.update_numbers = []
    }

    return resolved;
    }
};

module.exports = MmControl;
