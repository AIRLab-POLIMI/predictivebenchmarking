// Auto-generated. Do not edit!

// (in-package energy_mgmt.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class AuctionResult {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.winner = null;
    }
    else {
      if (initObj.hasOwnProperty('winner')) {
        this.winner = initObj.winner
      }
      else {
        this.winner = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type AuctionResult
    // Serialize message field [winner]
    bufferOffset = _serializer.bool(obj.winner, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type AuctionResult
    let len;
    let data = new AuctionResult(null);
    // Deserialize message field [winner]
    data.winner = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a message object
    return 'energy_mgmt/AuctionResult';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '970386071cec2ebdf79afc8a0312c15a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool winner
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new AuctionResult(null);
    if (msg.winner !== undefined) {
      resolved.winner = msg.winner;
    }
    else {
      resolved.winner = false
    }

    return resolved;
    }
};

module.exports = AuctionResult;
