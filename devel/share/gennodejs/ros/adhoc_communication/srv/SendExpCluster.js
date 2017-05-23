// Auto-generated. Do not edit!

// (in-package adhoc_communication.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ExpCluster = require('../msg/ExpCluster.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SendExpClusterRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.topic = null;
      this.dst_robot = null;
      this.cluster = null;
    }
    else {
      if (initObj.hasOwnProperty('topic')) {
        this.topic = initObj.topic
      }
      else {
        this.topic = '';
      }
      if (initObj.hasOwnProperty('dst_robot')) {
        this.dst_robot = initObj.dst_robot
      }
      else {
        this.dst_robot = '';
      }
      if (initObj.hasOwnProperty('cluster')) {
        this.cluster = initObj.cluster
      }
      else {
        this.cluster = new ExpCluster();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SendExpClusterRequest
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [dst_robot]
    bufferOffset = _serializer.string(obj.dst_robot, buffer, bufferOffset);
    // Serialize message field [cluster]
    bufferOffset = ExpCluster.serialize(obj.cluster, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendExpClusterRequest
    let len;
    let data = new SendExpClusterRequest(null);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [dst_robot]
    data.dst_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [cluster]
    data.cluster = ExpCluster.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.topic.length;
    length += object.dst_robot.length;
    length += ExpCluster.getMessageSize(object.cluster);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendExpClusterRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd1172e2fa3a1e03e6528ece001803f85';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string topic
    string dst_robot
    adhoc_communication/ExpCluster cluster
    
    ================================================================================
    MSG: adhoc_communication/ExpCluster
    ExpClusterElement[] ids_contained
    float64 bid 
    
    ================================================================================
    MSG: adhoc_communication/ExpClusterElement
    int64 id
    string detected_by_robot_str
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SendExpClusterRequest(null);
    if (msg.topic !== undefined) {
      resolved.topic = msg.topic;
    }
    else {
      resolved.topic = ''
    }

    if (msg.dst_robot !== undefined) {
      resolved.dst_robot = msg.dst_robot;
    }
    else {
      resolved.dst_robot = ''
    }

    if (msg.cluster !== undefined) {
      resolved.cluster = ExpCluster.Resolve(msg.cluster)
    }
    else {
      resolved.cluster = new ExpCluster()
    }

    return resolved;
    }
};

class SendExpClusterResponse {
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
    // Serializes a message object of type SendExpClusterResponse
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendExpClusterResponse
    let len;
    let data = new SendExpClusterResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendExpClusterResponse';
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
    const resolved = new SendExpClusterResponse(null);
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
  Request: SendExpClusterRequest,
  Response: SendExpClusterResponse,
  md5sum() { return '356dd4b5adb461bab3c183a7d7c21532'; },
  datatype() { return 'adhoc_communication/SendExpCluster'; }
};
