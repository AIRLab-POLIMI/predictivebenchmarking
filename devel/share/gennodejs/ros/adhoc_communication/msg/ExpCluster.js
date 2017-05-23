// Auto-generated. Do not edit!

// (in-package adhoc_communication.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let ExpClusterElement = require('./ExpClusterElement.js');

//-----------------------------------------------------------

class ExpCluster {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.ids_contained = null;
      this.bid = null;
    }
    else {
      if (initObj.hasOwnProperty('ids_contained')) {
        this.ids_contained = initObj.ids_contained
      }
      else {
        this.ids_contained = [];
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
    // Serializes a message object of type ExpCluster
    // Serialize message field [ids_contained]
    // Serialize the length for message field [ids_contained]
    bufferOffset = _serializer.uint32(obj.ids_contained.length, buffer, bufferOffset);
    obj.ids_contained.forEach((val) => {
      bufferOffset = ExpClusterElement.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [bid]
    bufferOffset = _serializer.float64(obj.bid, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ExpCluster
    let len;
    let data = new ExpCluster(null);
    // Deserialize message field [ids_contained]
    // Deserialize array length for message field [ids_contained]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.ids_contained = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.ids_contained[i] = ExpClusterElement.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [bid]
    data.bid = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.ids_contained.forEach((val) => {
      length += ExpClusterElement.getMessageSize(val);
    });
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'adhoc_communication/ExpCluster';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '378b1f01ebed06706a22e7cc27608df5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new ExpCluster(null);
    if (msg.ids_contained !== undefined) {
      resolved.ids_contained = new Array(msg.ids_contained.length);
      for (let i = 0; i < resolved.ids_contained.length; ++i) {
        resolved.ids_contained[i] = ExpClusterElement.Resolve(msg.ids_contained[i]);
      }
    }
    else {
      resolved.ids_contained = []
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

module.exports = ExpCluster;
