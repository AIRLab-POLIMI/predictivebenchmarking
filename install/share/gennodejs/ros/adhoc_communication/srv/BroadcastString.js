// Auto-generated. Do not edit!

// (in-package adhoc_communication.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class BroadcastStringRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.topic = null;
      this.data = null;
      this.hop_limit = null;
    }
    else {
      if (initObj.hasOwnProperty('topic')) {
        this.topic = initObj.topic
      }
      else {
        this.topic = '';
      }
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = '';
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
    // Serializes a message object of type BroadcastStringRequest
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [data]
    bufferOffset = _serializer.string(obj.data, buffer, bufferOffset);
    // Serialize message field [hop_limit]
    bufferOffset = _serializer.uint8(obj.hop_limit, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BroadcastStringRequest
    let len;
    let data = new BroadcastStringRequest(null);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [data]
    data.data = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [hop_limit]
    data.hop_limit = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.topic.length;
    length += object.data.length;
    return length + 9;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/BroadcastStringRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7e8adfc00ec8a3999ce5ae0ea2e708c7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string topic
    string data
    uint8 hop_limit
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new BroadcastStringRequest(null);
    if (msg.topic !== undefined) {
      resolved.topic = msg.topic;
    }
    else {
      resolved.topic = ''
    }

    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = ''
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

class BroadcastStringResponse {
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
    // Serializes a message object of type BroadcastStringResponse
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type BroadcastStringResponse
    let len;
    let data = new BroadcastStringResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/BroadcastStringResponse';
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
    const resolved = new BroadcastStringResponse(null);
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
  Request: BroadcastStringRequest,
  Response: BroadcastStringResponse,
  md5sum() { return '79e1c1b930819d5a990dea57200bd10a'; },
  datatype() { return 'adhoc_communication/BroadcastString'; }
};
