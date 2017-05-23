// Auto-generated. Do not edit!

// (in-package map_merger.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let adhoc_communication = _finder('adhoc_communication');

//-----------------------------------------------------------


//-----------------------------------------------------------

class TransformPointRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.point = null;
    }
    else {
      if (initObj.hasOwnProperty('point')) {
        this.point = initObj.point
      }
      else {
        this.point = new adhoc_communication.msg.MmPoint();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TransformPointRequest
    // Serialize message field [point]
    bufferOffset = adhoc_communication.msg.MmPoint.serialize(obj.point, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TransformPointRequest
    let len;
    let data = new TransformPointRequest(null);
    // Deserialize message field [point]
    data.point = adhoc_communication.msg.MmPoint.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += adhoc_communication.msg.MmPoint.getMessageSize(object.point);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'map_merger/TransformPointRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ff0adb045fabd1e2f01bd484ef29c081';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    adhoc_communication/MmPoint point
    
    ================================================================================
    MSG: adhoc_communication/MmPoint
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
    const resolved = new TransformPointRequest(null);
    if (msg.point !== undefined) {
      resolved.point = adhoc_communication.msg.MmPoint.Resolve(msg.point)
    }
    else {
      resolved.point = new adhoc_communication.msg.MmPoint()
    }

    return resolved;
    }
};

class TransformPointResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.point = null;
    }
    else {
      if (initObj.hasOwnProperty('point')) {
        this.point = initObj.point
      }
      else {
        this.point = new adhoc_communication.msg.MmPoint();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TransformPointResponse
    // Serialize message field [point]
    bufferOffset = adhoc_communication.msg.MmPoint.serialize(obj.point, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TransformPointResponse
    let len;
    let data = new TransformPointResponse(null);
    // Deserialize message field [point]
    data.point = adhoc_communication.msg.MmPoint.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += adhoc_communication.msg.MmPoint.getMessageSize(object.point);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'map_merger/TransformPointResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ff0adb045fabd1e2f01bd484ef29c081';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    adhoc_communication/MmPoint point
    
    
    ================================================================================
    MSG: adhoc_communication/MmPoint
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
    const resolved = new TransformPointResponse(null);
    if (msg.point !== undefined) {
      resolved.point = adhoc_communication.msg.MmPoint.Resolve(msg.point)
    }
    else {
      resolved.point = new adhoc_communication.msg.MmPoint()
    }

    return resolved;
    }
};

module.exports = {
  Request: TransformPointRequest,
  Response: TransformPointResponse,
  md5sum() { return '118b08a194ba8d774bcc2a526a4b8444'; },
  datatype() { return 'map_merger/TransformPoint'; }
};
