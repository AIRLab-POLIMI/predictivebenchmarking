// Generated by gencpp from file adhoc_communication/ExpClusterElement.msg
// DO NOT EDIT!


#ifndef ADHOC_COMMUNICATION_MESSAGE_EXPCLUSTERELEMENT_H
#define ADHOC_COMMUNICATION_MESSAGE_EXPCLUSTERELEMENT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace adhoc_communication
{
template <class ContainerAllocator>
struct ExpClusterElement_
{
  typedef ExpClusterElement_<ContainerAllocator> Type;

  ExpClusterElement_()
    : id(0)
    , detected_by_robot_str()  {
    }
  ExpClusterElement_(const ContainerAllocator& _alloc)
    : id(0)
    , detected_by_robot_str(_alloc)  {
  (void)_alloc;
    }



   typedef int64_t _id_type;
  _id_type id;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _detected_by_robot_str_type;
  _detected_by_robot_str_type detected_by_robot_str;




  typedef boost::shared_ptr< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> const> ConstPtr;

}; // struct ExpClusterElement_

typedef ::adhoc_communication::ExpClusterElement_<std::allocator<void> > ExpClusterElement;

typedef boost::shared_ptr< ::adhoc_communication::ExpClusterElement > ExpClusterElementPtr;
typedef boost::shared_ptr< ::adhoc_communication::ExpClusterElement const> ExpClusterElementConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::adhoc_communication::ExpClusterElement_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace adhoc_communication

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'adhoc_communication': ['/home/valerio/slampbenchmarking/src/aau_multi_robot/adhoc_communication/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> >
{
  static const char* value()
  {
    return "4c7924311e9f149f7f5025e4bf173fd7";
  }

  static const char* value(const ::adhoc_communication::ExpClusterElement_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x4c7924311e9f149fULL;
  static const uint64_t static_value2 = 0x7f5025e4bf173fd7ULL;
};

template<class ContainerAllocator>
struct DataType< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> >
{
  static const char* value()
  {
    return "adhoc_communication/ExpClusterElement";
  }

  static const char* value(const ::adhoc_communication::ExpClusterElement_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 id\n\
string detected_by_robot_str\n\
";
  }

  static const char* value(const ::adhoc_communication::ExpClusterElement_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.id);
      stream.next(m.detected_by_robot_str);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ExpClusterElement_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::adhoc_communication::ExpClusterElement_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::adhoc_communication::ExpClusterElement_<ContainerAllocator>& v)
  {
    s << indent << "id: ";
    Printer<int64_t>::stream(s, indent + "  ", v.id);
    s << indent << "detected_by_robot_str: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.detected_by_robot_str);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ADHOC_COMMUNICATION_MESSAGE_EXPCLUSTERELEMENT_H
