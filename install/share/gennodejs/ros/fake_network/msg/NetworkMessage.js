// Auto-generated. Do not edit!

// (in-package fake_network.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class NetworkMessage {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.source_robot = null;
      this.payload = null;
      this.data_type = null;
      this.topic = null;
    }
    else {
      if (initObj.hasOwnProperty('source_robot')) {
        this.source_robot = initObj.source_robot
      }
      else {
        this.source_robot = '';
      }
      if (initObj.hasOwnProperty('payload')) {
        this.payload = initObj.payload
      }
      else {
        this.payload = '';
      }
      if (initObj.hasOwnProperty('data_type')) {
        this.data_type = initObj.data_type
      }
      else {
        this.data_type = 0;
      }
      if (initObj.hasOwnProperty('topic')) {
        this.topic = initObj.topic
      }
      else {
        this.topic = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type NetworkMessage
    // Serialize message field [source_robot]
    bufferOffset = _serializer.string(obj.source_robot, buffer, bufferOffset);
    // Serialize message field [payload]
    bufferOffset = _serializer.string(obj.payload, buffer, bufferOffset);
    // Serialize message field [data_type]
    bufferOffset = _serializer.uint8(obj.data_type, buffer, bufferOffset);
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type NetworkMessage
    let len;
    let data = new NetworkMessage(null);
    // Deserialize message field [source_robot]
    data.source_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [payload]
    data.payload = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [data_type]
    data.data_type = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.source_robot.length;
    length += object.payload.length;
    length += object.topic.length;
    return length + 13;
  }

  static datatype() {
    // Returns string type for a message object
    return 'fake_network/NetworkMessage';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '67d28fd41fb2346145ecac16f2c7c957';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string source_robot
    string payload
    uint8 data_type
    string topic
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new NetworkMessage(null);
    if (msg.source_robot !== undefined) {
      resolved.source_robot = msg.source_robot;
    }
    else {
      resolved.source_robot = ''
    }

    if (msg.payload !== undefined) {
      resolved.payload = msg.payload;
    }
    else {
      resolved.payload = ''
    }

    if (msg.data_type !== undefined) {
      resolved.data_type = msg.data_type;
    }
    else {
      resolved.data_type = 0
    }

    if (msg.topic !== undefined) {
      resolved.topic = msg.topic;
    }
    else {
      resolved.topic = ''
    }

    return resolved;
    }
};

module.exports = NetworkMessage;
