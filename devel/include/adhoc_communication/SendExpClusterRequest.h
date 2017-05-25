// Generated by gencpp from file adhoc_communication/SendExpClusterRequest.msg
// DO NOT EDIT!


#ifndef ADHOC_COMMUNICATION_MESSAGE_SENDEXPCLUSTERREQUEST_H
#define ADHOC_COMMUNICATION_MESSAGE_SENDEXPCLUSTERREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <adhoc_communication/ExpCluster.h>

namespace adhoc_communication
{
template <class ContainerAllocator>
struct SendExpClusterRequest_
{
  typedef SendExpClusterRequest_<ContainerAllocator> Type;

  SendExpClusterRequest_()
    : topic()
    , dst_robot()
    , cluster()  {
    }
  SendExpClusterRequest_(const ContainerAllocator& _alloc)
    : topic(_alloc)
    , dst_robot(_alloc)
    , cluster(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _topic_type;
  _topic_type topic;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _dst_robot_type;
  _dst_robot_type dst_robot;

   typedef  ::adhoc_communication::ExpCluster_<ContainerAllocator>  _cluster_type;
  _cluster_type cluster;




  typedef boost::shared_ptr< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SendExpClusterRequest_

typedef ::adhoc_communication::SendExpClusterRequest_<std::allocator<void> > SendExpClusterRequest;

typedef boost::shared_ptr< ::adhoc_communication::SendExpClusterRequest > SendExpClusterRequestPtr;
typedef boost::shared_ptr< ::adhoc_communication::SendExpClusterRequest const> SendExpClusterRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace adhoc_communication

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'adhoc_communication': ['/home/ros/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d1172e2fa3a1e03e6528ece001803f85";
  }

  static const char* value(const ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd1172e2fa3a1e03eULL;
  static const uint64_t static_value2 = 0x6528ece001803f85ULL;
};

template<class ContainerAllocator>
struct DataType< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "adhoc_communication/SendExpClusterRequest";
  }

  static const char* value(const ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string topic\n\
string dst_robot\n\
adhoc_communication/ExpCluster cluster\n\
\n\
================================================================================\n\
MSG: adhoc_communication/ExpCluster\n\
ExpClusterElement[] ids_contained\n\
float64 bid \n\
\n\
================================================================================\n\
MSG: adhoc_communication/ExpClusterElement\n\
int64 id\n\
string detected_by_robot_str\n\
";
  }

  static const char* value(const ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.topic);
      stream.next(m.dst_robot);
      stream.next(m.cluster);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SendExpClusterRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::adhoc_communication::SendExpClusterRequest_<ContainerAllocator>& v)
  {
    s << indent << "topic: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.topic);
    s << indent << "dst_robot: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.dst_robot);
    s << indent << "cluster: ";
    s << std::endl;
    Printer< ::adhoc_communication::ExpCluster_<ContainerAllocator> >::stream(s, indent + "  ", v.cluster);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ADHOC_COMMUNICATION_MESSAGE_SENDEXPCLUSTERREQUEST_H
