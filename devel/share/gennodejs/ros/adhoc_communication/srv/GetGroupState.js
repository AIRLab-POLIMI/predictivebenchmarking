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

class GetGroupStateRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.group_name = null;
    }
    else {
      if (initObj.hasOwnProperty('group_name')) {
        this.group_name = initObj.group_name
      }
      else {
        this.group_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetGroupStateRequest
    // Serialize message field [group_name]
    bufferOffset = _serializer.string(obj.group_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetGroupStateRequest
    let len;
    let data = new GetGroupStateRequest(null);
    // Deserialize message field [group_name]
    data.group_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.group_name.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/GetGroupStateRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '967d0b0c0d858ded8a6a69abbce0c981';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string group_name
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetGroupStateRequest(null);
    if (msg.group_name !== undefined) {
      resolved.group_name = msg.group_name;
    }
    else {
      resolved.group_name = ''
    }

    return resolved;
    }
};

class GetGroupStateResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.member = null;
      this.activated = null;
      this.connected = null;
      this.root = null;
      this.joining = null;
      this.route_uplink = null;
      this.downlinks = null;
    }
    else {
      if (initObj.hasOwnProperty('member')) {
        this.member = initObj.member
      }
      else {
        this.member = false;
      }
      if (initObj.hasOwnProperty('activated')) {
        this.activated = initObj.activated
      }
      else {
        this.activated = false;
      }
      if (initObj.hasOwnProperty('connected')) {
        this.connected = initObj.connected
      }
      else {
        this.connected = false;
      }
      if (initObj.hasOwnProperty('root')) {
        this.root = initObj.root
      }
      else {
        this.root = false;
      }
      if (initObj.hasOwnProperty('joining')) {
        this.joining = initObj.joining
      }
      else {
        this.joining = false;
      }
      if (initObj.hasOwnProperty('route_uplink')) {
        this.route_uplink = initObj.route_uplink
      }
      else {
        this.route_uplink = '';
      }
      if (initObj.hasOwnProperty('downlinks')) {
        this.downlinks = initObj.downlinks
      }
      else {
        this.downlinks = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GetGroupStateResponse
    // Serialize message field [member]
    bufferOffset = _serializer.bool(obj.member, buffer, bufferOffset);
    // Serialize message field [activated]
    bufferOffset = _serializer.bool(obj.activated, buffer, bufferOffset);
    // Serialize message field [connected]
    bufferOffset = _serializer.bool(obj.connected, buffer, bufferOffset);
    // Serialize message field [root]
    bufferOffset = _serializer.bool(obj.root, buffer, bufferOffset);
    // Serialize message field [joining]
    bufferOffset = _serializer.bool(obj.joining, buffer, bufferOffset);
    // Serialize message field [route_uplink]
    bufferOffset = _serializer.string(obj.route_uplink, buffer, bufferOffset);
    // Serialize message field [downlinks]
    bufferOffset = _arraySerializer.string(obj.downlinks, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GetGroupStateResponse
    let len;
    let data = new GetGroupStateResponse(null);
    // Deserialize message field [member]
    data.member = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [activated]
    data.activated = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [connected]
    data.connected = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [root]
    data.root = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [joining]
    data.joining = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [route_uplink]
    data.route_uplink = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [downlinks]
    data.downlinks = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.route_uplink.length;
    object.downlinks.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 13;
  }

  static datatype() {
    // Returns string type for a service object
    return 'adhoc_communication/GetGroupStateResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a60c9124520fea5a021262dcbe436318';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool member
    bool activated
    bool connected
    bool root
    bool joining
    string route_uplink
    string[] downlinks
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GetGroupStateResponse(null);
    if (msg.member !== undefined) {
      resolved.member = msg.member;
    }
    else {
      resolved.member = false
    }

    if (msg.activated !== undefined) {
      resolved.activated = msg.activated;
    }
    else {
      resolved.activated = false
    }

    if (msg.connected !== undefined) {
      resolved.connected = msg.connected;
    }
    else {
      resolved.connected = false
    }

    if (msg.root !== undefined) {
      resolved.root = msg.root;
    }
    else {
      resolved.root = false
    }

    if (msg.joining !== undefined) {
      resolved.joining = msg.joining;
    }
    else {
      resolved.joining = false
    }

    if (msg.route_uplink !== undefined) {
      resolved.route_uplink = msg.route_uplink;
    }
    else {
      resolved.route_uplink = ''
    }

    if (msg.downlinks !== undefined) {
      resolved.downlinks = msg.downlinks;
    }
    else {
      resolved.downlinks = []
    }

    return resolved;
    }
};

module.exports = {
  Request: GetGroupStateRequest,
  Response: GetGroupStateResponse,
  md5sum() { return '3fd78af244ca7820f4d762caa767ec74'; },
  datatype() { return 'adhoc_communication/GetGroupState'; }
};
