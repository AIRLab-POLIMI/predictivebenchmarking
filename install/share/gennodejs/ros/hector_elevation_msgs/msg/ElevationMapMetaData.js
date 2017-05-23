// Auto-generated. Do not edit!

// (in-package hector_elevation_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class ElevationMapMetaData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.map_load_time = null;
      this.resolution_xy = null;
      this.resolution_z = null;
      this.min_elevation = null;
      this.max_elevation = null;
      this.zero_elevation = null;
      this.width = null;
      this.height = null;
      this.origin = null;
    }
    else {
      if (initObj.hasOwnProperty('map_load_time')) {
        this.map_load_time = initObj.map_load_time
      }
      else {
        this.map_load_time = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('resolution_xy')) {
        this.resolution_xy = initObj.resolution_xy
      }
      else {
        this.resolution_xy = 0.0;
      }
      if (initObj.hasOwnProperty('resolution_z')) {
        this.resolution_z = initObj.resolution_z
      }
      else {
        this.resolution_z = 0.0;
      }
      if (initObj.hasOwnProperty('min_elevation')) {
        this.min_elevation = initObj.min_elevation
      }
      else {
        this.min_elevation = 0.0;
      }
      if (initObj.hasOwnProperty('max_elevation')) {
        this.max_elevation = initObj.max_elevation
      }
      else {
        this.max_elevation = 0.0;
      }
      if (initObj.hasOwnProperty('zero_elevation')) {
        this.zero_elevation = initObj.zero_elevation
      }
      else {
        this.zero_elevation = 0;
      }
      if (initObj.hasOwnProperty('width')) {
        this.width = initObj.width
      }
      else {
        this.width = 0;
      }
      if (initObj.hasOwnProperty('height')) {
        this.height = initObj.height
      }
      else {
        this.height = 0;
      }
      if (initObj.hasOwnProperty('origin')) {
        this.origin = initObj.origin
      }
      else {
        this.origin = new geometry_msgs.msg.Pose();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ElevationMapMetaData
    // Serialize message field [map_load_time]
    bufferOffset = _serializer.time(obj.map_load_time, buffer, bufferOffset);
    // Serialize message field [resolution_xy]
    bufferOffset = _serializer.float64(obj.resolution_xy, buffer, bufferOffset);
    // Serialize message field [resolution_z]
    bufferOffset = _serializer.float64(obj.resolution_z, buffer, bufferOffset);
    // Serialize message field [min_elevation]
    bufferOffset = _serializer.float64(obj.min_elevation, buffer, bufferOffset);
    // Serialize message field [max_elevation]
    bufferOffset = _serializer.float64(obj.max_elevation, buffer, bufferOffset);
    // Serialize message field [zero_elevation]
    bufferOffset = _serializer.int16(obj.zero_elevation, buffer, bufferOffset);
    // Serialize message field [width]
    bufferOffset = _serializer.uint32(obj.width, buffer, bufferOffset);
    // Serialize message field [height]
    bufferOffset = _serializer.uint32(obj.height, buffer, bufferOffset);
    // Serialize message field [origin]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.origin, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ElevationMapMetaData
    let len;
    let data = new ElevationMapMetaData(null);
    // Deserialize message field [map_load_time]
    data.map_load_time = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [resolution_xy]
    data.resolution_xy = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [resolution_z]
    data.resolution_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [min_elevation]
    data.min_elevation = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [max_elevation]
    data.max_elevation = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [zero_elevation]
    data.zero_elevation = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [width]
    data.width = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [height]
    data.height = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [origin]
    data.origin = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 106;
  }

  static datatype() {
    // Returns string type for a message object
    return 'hector_elevation_msgs/ElevationMapMetaData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6c887873faf3a1d55d884bdcc92b9241';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # This hold basic information about the characterists of the EvaluationGrid
    
    # The time at which the map was loaded
    time map_load_time
    # Map resolution in xy plane [m/cell]
    float64 resolution_xy
    # Map resolution in height [m/cell]
    float64 resolution_z
    # min observed height [m]
    float64 min_elevation
    # max observed height [m]
    float64 max_elevation
    # Height zero value. For example 16384.
    int16 zero_elevation
    # Map width [cells]
    uint32 width
    # Map height [cells]
    uint32 height
    # The origin of the map [m, m, rad].  This is the real-world pose of the
    # cell (0,0) in the map.
    geometry_msgs/Pose origin
    
    
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ElevationMapMetaData(null);
    if (msg.map_load_time !== undefined) {
      resolved.map_load_time = msg.map_load_time;
    }
    else {
      resolved.map_load_time = {secs: 0, nsecs: 0}
    }

    if (msg.resolution_xy !== undefined) {
      resolved.resolution_xy = msg.resolution_xy;
    }
    else {
      resolved.resolution_xy = 0.0
    }

    if (msg.resolution_z !== undefined) {
      resolved.resolution_z = msg.resolution_z;
    }
    else {
      resolved.resolution_z = 0.0
    }

    if (msg.min_elevation !== undefined) {
      resolved.min_elevation = msg.min_elevation;
    }
    else {
      resolved.min_elevation = 0.0
    }

    if (msg.max_elevation !== undefined) {
      resolved.max_elevation = msg.max_elevation;
    }
    else {
      resolved.max_elevation = 0.0
    }

    if (msg.zero_elevation !== undefined) {
      resolved.zero_elevation = msg.zero_elevation;
    }
    else {
      resolved.zero_elevation = 0
    }

    if (msg.width !== undefined) {
      resolved.width = msg.width;
    }
    else {
      resolved.width = 0
    }

    if (msg.height !== undefined) {
      resolved.height = msg.height;
    }
    else {
      resolved.height = 0
    }

    if (msg.origin !== undefined) {
      resolved.origin = geometry_msgs.msg.Pose.Resolve(msg.origin)
    }
    else {
      resolved.origin = new geometry_msgs.msg.Pose()
    }

    return resolved;
    }
};

module.exports = ElevationMapMetaData;
