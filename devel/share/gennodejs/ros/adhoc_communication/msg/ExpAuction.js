// Auto-generated. Do not edit!

// (in-package adhoc_communication.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ExpAuctionElement = require('./ExpAuctionElement.js');
let ExpCluster = require('./ExpCluster.js');

//-----------------------------------------------------------

class ExpAuction {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.auction_status_message = null;
      this.start_auction = null;
      this.auction_finished = null;
      this.occupied_ids = null;
      this.requested_clusters = null;
      this.auction_id = null;
      this.robot_name = null;
      this.available_clusters = null;
    }
    else {
      if (initObj.hasOwnProperty('auction_status_message')) {
        this.auction_status_message = initObj.auction_status_message
      }
      else {
        this.auction_status_message = false;
      }
      if (initObj.hasOwnProperty('start_auction')) {
        this.start_auction = initObj.start_auction
      }
      else {
        this.start_auction = false;
      }
      if (initObj.hasOwnProperty('auction_finished')) {
        this.auction_finished = initObj.auction_finished
      }
      else {
        this.auction_finished = false;
      }
      if (initObj.hasOwnProperty('occupied_ids')) {
        this.occupied_ids = initObj.occupied_ids
      }
      else {
        this.occupied_ids = [];
      }
      if (initObj.hasOwnProperty('requested_clusters')) {
        this.requested_clusters = initObj.requested_clusters
      }
      else {
        this.requested_clusters = [];
      }
      if (initObj.hasOwnProperty('auction_id')) {
        this.auction_id = initObj.auction_id
      }
      else {
        this.auction_id = 0;
      }
      if (initObj.hasOwnProperty('robot_name')) {
        this.robot_name = initObj.robot_name
      }
      else {
        this.robot_name = '';
      }
      if (initObj.hasOwnProperty('available_clusters')) {
        this.available_clusters = initObj.available_clusters
      }
      else {
        this.available_clusters = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ExpAuction
    // Serialize message field [auction_status_message]
    bufferOffset = _serializer.bool(obj.auction_status_message, buffer, bufferOffset);
    // Serialize message field [start_auction]
    bufferOffset = _serializer.bool(obj.start_auction, buffer, bufferOffset);
    // Serialize message field [auction_finished]
    bufferOffset = _serializer.bool(obj.auction_finished, buffer, bufferOffset);
    // Serialize message field [occupied_ids]
    // Serialize the length for message field [occupied_ids]
    bufferOffset = _serializer.uint32(obj.occupied_ids.length, buffer, bufferOffset);
    obj.occupied_ids.forEach((val) => {
      bufferOffset = ExpAuctionElement.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [requested_clusters]
    // Serialize the length for message field [requested_clusters]
    bufferOffset = _serializer.uint32(obj.requested_clusters.length, buffer, bufferOffset);
    obj.requested_clusters.forEach((val) => {
      bufferOffset = ExpCluster.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [auction_id]
    bufferOffset = _serializer.uint32(obj.auction_id, buffer, bufferOffset);
    // Serialize message field [robot_name]
    bufferOffset = _serializer.string(obj.robot_name, buffer, bufferOffset);
    // Serialize message field [available_clusters]
    // Serialize the length for message field [available_clusters]
    bufferOffset = _serializer.uint32(obj.available_clusters.length, buffer, bufferOffset);
    obj.available_clusters.forEach((val) => {
      bufferOffset = ExpCluster.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ExpAuction
    let len;
    let data = new ExpAuction(null);
    // Deserialize message field [auction_status_message]
    data.auction_status_message = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [start_auction]
    data.start_auction = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [auction_finished]
    data.auction_finished = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [occupied_ids]
    // Deserialize array length for message field [occupied_ids]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.occupied_ids = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.occupied_ids[i] = ExpAuctionElement.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [requested_clusters]
    // Deserialize array length for message field [requested_clusters]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.requested_clusters = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.requested_clusters[i] = ExpCluster.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [auction_id]
    data.auction_id = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [robot_name]
    data.robot_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [available_clusters]
    // Deserialize array length for message field [available_clusters]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.available_clusters = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.available_clusters[i] = ExpCluster.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.occupied_ids.forEach((val) => {
      length += ExpAuctionElement.getMessageSize(val);
    });
    object.requested_clusters.forEach((val) => {
      length += ExpCluster.getMessageSize(val);
    });
    length += object.robot_name.length;
    object.available_clusters.forEach((val) => {
      length += ExpCluster.getMessageSize(val);
    });
    return length + 23;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/ExpAuction';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '99f1253490d52d5e7eb6095beeea2711';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new ExpAuction(null);
    if (msg.auction_status_message !== undefined) {
      resolved.auction_status_message = msg.auction_status_message;
    }
    else {
      resolved.auction_status_message = false
    }

    if (msg.start_auction !== undefined) {
      resolved.start_auction = msg.start_auction;
    }
    else {
      resolved.start_auction = false
    }

    if (msg.auction_finished !== undefined) {
      resolved.auction_finished = msg.auction_finished;
    }
    else {
      resolved.auction_finished = false
    }

    if (msg.occupied_ids !== undefined) {
      resolved.occupied_ids = new Array(msg.occupied_ids.length);
      for (let i = 0; i < resolved.occupied_ids.length; ++i) {
        resolved.occupied_ids[i] = ExpAuctionElement.Resolve(msg.occupied_ids[i]);
      }
    }
    else {
      resolved.occupied_ids = []
    }

    if (msg.requested_clusters !== undefined) {
      resolved.requested_clusters = new Array(msg.requested_clusters.length);
      for (let i = 0; i < resolved.requested_clusters.length; ++i) {
        resolved.requested_clusters[i] = ExpCluster.Resolve(msg.requested_clusters[i]);
      }
    }
    else {
      resolved.requested_clusters = []
    }

    if (msg.auction_id !== undefined) {
      resolved.auction_id = msg.auction_id;
    }
    else {
      resolved.auction_id = 0
    }

    if (msg.robot_name !== undefined) {
      resolved.robot_name = msg.robot_name;
    }
    else {
      resolved.robot_name = ''
    }

    if (msg.available_clusters !== undefined) {
      resolved.available_clusters = new Array(msg.available_clusters.length);
      for (let i = 0; i < resolved.available_clusters.length; ++i) {
        resolved.available_clusters[i] = ExpCluster.Resolve(msg.available_clusters[i]);
      }
    }
    else {
      resolved.available_clusters = []
    }

    return resolved;
    }
};

module.exports = ExpAuction;
