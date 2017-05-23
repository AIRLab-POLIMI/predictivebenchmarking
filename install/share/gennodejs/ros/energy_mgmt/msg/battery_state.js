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

class battery_state {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.charging = null;
      this.soc = null;
      this.remaining_time_charge = null;
      this.remaining_time_run = null;
      this.remaining_distance = null;
    }
    else {
      if (initObj.hasOwnProperty('charging')) {
        this.charging = initObj.charging
      }
      else {
        this.charging = false;
      }
      if (initObj.hasOwnProperty('soc')) {
        this.soc = initObj.soc
      }
      else {
        this.soc = 0.0;
      }
      if (initObj.hasOwnProperty('remaining_time_charge')) {
        this.remaining_time_charge = initObj.remaining_time_charge
      }
      else {
        this.remaining_time_charge = 0.0;
      }
      if (initObj.hasOwnProperty('remaining_time_run')) {
        this.remaining_time_run = initObj.remaining_time_run
      }
      else {
        this.remaining_time_run = 0.0;
      }
      if (initObj.hasOwnProperty('remaining_distance')) {
        this.remaining_distance = initObj.remaining_distance
      }
      else {
        this.remaining_distance = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type battery_state
    // Serialize message field [charging]
    bufferOffset = _serializer.bool(obj.charging, buffer, bufferOffset);
    // Serialize message field [soc]
    bufferOffset = _serializer.float32(obj.soc, buffer, bufferOffset);
    // Serialize message field [remaining_time_charge]
    bufferOffset = _serializer.float32(obj.remaining_time_charge, buffer, bufferOffset);
    // Serialize message field [remaining_time_run]
    bufferOffset = _serializer.float32(obj.remaining_time_run, buffer, bufferOffset);
    // Serialize message field [remaining_distance]
    bufferOffset = _serializer.float32(obj.remaining_distance, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type battery_state
    let len;
    let data = new battery_state(null);
    // Deserialize message field [charging]
    data.charging = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [soc]
    data.soc = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [remaining_time_charge]
    data.remaining_time_charge = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [remaining_time_run]
    data.remaining_time_run = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [remaining_distance]
    data.remaining_distance = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 17;
  }

  static datatype() {
    // Returns string type for a message object
    return 'energy_mgmt/battery_state';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ae34ca1536c302c535b231631ea2d4bc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool charging
    float32 soc
    float32 remaining_time_charge
    float32 remaining_time_run
    float32 remaining_distance
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new battery_state(null);
    if (msg.charging !== undefined) {
      resolved.charging = msg.charging;
    }
    else {
      resolved.charging = false
    }

    if (msg.soc !== undefined) {
      resolved.soc = msg.soc;
    }
    else {
      resolved.soc = 0.0
    }

    if (msg.remaining_time_charge !== undefined) {
      resolved.remaining_time_charge = msg.remaining_time_charge;
    }
    else {
      resolved.remaining_time_charge = 0.0
    }

    if (msg.remaining_time_run !== undefined) {
      resolved.remaining_time_run = msg.remaining_time_run;
    }
    else {
      resolved.remaining_time_run = 0.0
    }

    if (msg.remaining_distance !== undefined) {
      resolved.remaining_distance = msg.remaining_distance;
    }
    else {
      resolved.remaining_distance = 0.0
    }

    return resolved;
    }
};

module.exports = battery_state;
