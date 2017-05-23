// Auto-generated. Do not edit!

// (in-package map_merger.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class LogMapsRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.log = null;
    }
    else {
      if (initObj.hasOwnProperty('log')) {
        this.log = initObj.log
      }
      else {
        this.log = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LogMapsRequest
    // Serialize message field [log]
    bufferOffset = _serializer.uint16(obj.log, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LogMapsRequest
    let len;
    let data = new LogMapsRequest(null);
    // Deserialize message field [log]
    data.log = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 2;
  }

  static datatype() {
    // Returns string type for a service object
    return 'map_merger/LogMapsRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bb54d185c1070cbf70d4cfb2996c18fd';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint16 log
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LogMapsRequest(null);
    if (msg.log !== undefined) {
      resolved.log = msg.log;
    }
    else {
      resolved.log = 0
    }

    return resolved;
    }
};

class LogMapsResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type LogMapsResponse
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type LogMapsResponse
    let len;
    let data = new LogMapsResponse(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'map_merger/LogMapsResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new LogMapsResponse(null);
    return resolved;
    }
};

module.exports = {
  Request: LogMapsRequest,
  Response: LogMapsResponse,
  md5sum() { return 'bb54d185c1070cbf70d4cfb2996c18fd'; },
  datatype() { return 'map_merger/LogMaps'; }
};
