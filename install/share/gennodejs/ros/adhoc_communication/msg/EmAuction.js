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

class EmAuction {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.auction = null;
      this.robot = null;
      this.docking_station = null;
      this.bid = null;
    }
    else {
      if (initObj.hasOwnProperty('auction')) {
        this.auction = initObj.auction
      }
      else {
        this.auction = 0;
      }
      if (initObj.hasOwnProperty('robot')) {
        this.robot = initObj.robot
      }
      else {
        this.robot = 0;
      }
      if (initObj.hasOwnProperty('docking_station')) {
        this.docking_station = initObj.docking_station
      }
      else {
        this.docking_station = 0;
      }
      if (initObj.hasOwnProperty('bid')) {
        this.bid = initObj.bid
      }
      else {
        this.bid = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type EmAuction
    // Serialize message field [auction]
    bufferOffset = _serializer.uint32(obj.auction, buffer, bufferOffset);
    // Serialize message field [robot]
    bufferOffset = _serializer.uint32(obj.robot, buffer, bufferOffset);
    // Serialize message field [docking_station]
    bufferOffset = _serializer.uint32(obj.docking_station, buffer, bufferOffset);
    // Serialize message field [bid]
    bufferOffset = _serializer.float32(obj.bid, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type EmAuction
    let len;
    let data = new EmAuction(null);
    // Deserialize message field [auction]
    data.auction = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [robot]
    data.robot = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [docking_station]
    data.docking_station = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [bid]
    data.bid = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/EmAuction';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '942c2474214e04f260e8c0832e6a1dad';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint32 auction
    uint32 robot
    uint32 docking_station
    float32 bid
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new EmAuction(null);
    if (msg.auction !== undefined) {
      resolved.auction = msg.auction;
    }
    else {
      resolved.auction = 0
    }

    if (msg.robot !== undefined) {
      resolved.robot = msg.robot;
    }
    else {
      resolved.robot = 0
    }

    if (msg.docking_station !== undefined) {
      resolved.docking_station = msg.docking_station;
    }
    else {
      resolved.docking_station = 0
    }

    if (msg.bid !== undefined) {
      resolved.bid = msg.bid;
    }
    else {
      resolved.bid = 0.0
    }

    return resolved;
    }
};

module.exports = EmAuction;
