// Auto-generated. Do not edit!

// (in-package adhoc_communication.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ExpAuction = require('../msg/ExpAuction.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SendExpAuctionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.topic = null;
      this.dst_robot = null;
      this.auction = null;
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
      if (initObj.hasOwnProperty('auction')) {
        this.auction = initObj.auction
      }
      else {
        this.auction = new ExpAuction();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SendExpAuctionRequest
    // Serialize message field [topic]
    bufferOffset = _serializer.string(obj.topic, buffer, bufferOffset);
    // Serialize message field [dst_robot]
    bufferOffset = _serializer.string(obj.dst_robot, buffer, bufferOffset);
    // Serialize message field [auction]
    bufferOffset = ExpAuction.serialize(obj.auction, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendExpAuctionRequest
    let len;
    let data = new SendExpAuctionRequest(null);
    // Deserialize message field [topic]
    data.topic = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [dst_robot]
    data.dst_robot = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [auction]
    data.auction = ExpAuction.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.topic.length;
    length += object.dst_robot.length;
    length += ExpAuction.getMessageSize(object.auction);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendExpAuctionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '402f0303dc933f57bece3d13fe58db17';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string topic
    string dst_robot
    adhoc_communication/ExpAuction auction
    
    ================================================================================
    MSG: adhoc_communication/ExpAuction
    bool auction_status_message
    bool start_auction
    bool auction_finished
    ExpAuctionElement[] occupied_ids
    ExpCluster[] requested_clusters
    uint32 auction_id
    string robot_name
    ExpCluster[] available_clusters
    
    ================================================================================
    MSG: adhoc_communication/ExpAuctionElement
    int64 id
    string detected_by_robot_str
    
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
    const resolved = new SendExpAuctionRequest(null);
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

    if (msg.auction !== undefined) {
      resolved.auction = ExpAuction.Resolve(msg.auction)
    }
    else {
      resolved.auction = new ExpAuction()
    }

    return resolved;
    }
};

class SendExpAuctionResponse {
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
    // Serializes a message object of type SendExpAuctionResponse
    // Serialize message field [status]
    bufferOffset = _serializer.uint8(obj.status, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SendExpAuctionResponse
    let len;
    let data = new SendExpAuctionResponse(null);
    // Deserialize message field [status]
    data.status = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/SendExpAuctionResponse';
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
    const resolved = new SendExpAuctionResponse(null);
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
  Request: SendExpAuctionRequest,
  Response: SendExpAuctionResponse,
  md5sum() { return 'ff9ea50dac4ae5fb2075cab78b2fc2b9'; },
  datatype() { return 'adhoc_communication/SendExpAuction'; }
};
