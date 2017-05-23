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

class ExpClusterElement {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.id = null;
      this.detected_by_robot_str = null;
    }
    else {
      if (initObj.hasOwnProperty('id')) {
        this.id = initObj.id
      }
      else {
        this.id = 0;
      }
      if (initObj.hasOwnProperty('detected_by_robot_str')) {
        this.detected_by_robot_str = initObj.detected_by_robot_str
      }
      else {
        this.detected_by_robot_str = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ExpClusterElement
    // Serialize message field [id]
    bufferOffset = _serializer.int64(obj.id, buffer, bufferOffset);
    // Serialize message field [detected_by_robot_str]
    bufferOffset = _serializer.string(obj.detected_by_robot_str, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ExpClusterElement
    let len;
    let data = new ExpClusterElement(null);
    // Deserialize message field [id]
    data.id = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [detected_by_robot_str]
    data.detected_by_robot_str = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.detected_by_robot_str.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/ExpClusterElement';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4c7924311e9f149f7f5025e4bf173fd7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 id
    string detected_by_robot_str
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ExpClusterElement(null);
    if (msg.id !== undefined) {
      resolved.id = msg.id;
    }
    else {
      resolved.id = 0
    }

    if (msg.detected_by_robot_str !== undefined) {
      resolved.detected_by_robot_str = msg.detected_by_robot_str;
    }
    else {
      resolved.detected_by_robot_str = ''
    }

    return resolved;
    }
};

module.exports = ExpClusterElement;
