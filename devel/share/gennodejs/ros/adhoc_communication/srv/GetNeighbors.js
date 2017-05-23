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

class GetNeighborsRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetNeighborsRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetNeighborsRequest
    let len;
    let data = new GetNeighborsRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/GetNeighborsRequest';
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
    const resolved = new GetNeighborsRequest(null);
    return resolved;
    }
};

class GetNeighborsResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.neigbors = null;
    }
    else {
      if (initObj.hasOwnProperty('neigbors')) {
        this.neigbors = initObj.neigbors
      }
      else {
        this.neigbors = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetNeighborsResponse
    // Serialize message field [neigbors]
    bufferOffset = _arraySerializer.string(obj.neigbors, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetNeighborsResponse
    let len;
    let data = new GetNeighborsResponse(null);
    // Deserialize message field [neigbors]
    data.neigbors = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.neigbors.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/GetNeighborsResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a51be085cd4a0fb160e82a9e1952784d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] neigbors
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetNeighborsResponse(null);
    if (msg.neigbors !== undefined) {
      resolved.neigbors = msg.neigbors;
    }
    else {
      resolved.neigbors = []
    }

    return resolved;
    }
};

module.exports = {
  Request: GetNeighborsRequest,
  Response: GetNeighborsResponse,
  md5sum() { return 'a51be085cd4a0fb160e82a9e1952784d'; },
  datatype() { return 'adhoc_communication/GetNeighbors'; }
};
