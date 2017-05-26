// Generated by gencpp from file adhoc_communication/ExpAuction.msg
// DO NOT EDIT!


#ifndef ADHOC_COMMUNICATION_MESSAGE_EXPAUCTION_H
#define ADHOC_COMMUNICATION_MESSAGE_EXPAUCTION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <adhoc_communication/ExpAuctionElement.h>
#include <adhoc_communication/ExpCluster.h>
#include <adhoc_communication/ExpCluster.h>

namespace adhoc_communication
{
template <class ContainerAllocator>
struct ExpAuction_
{
  typedef ExpAuction_<ContainerAllocator> Type;

  ExpAuction_()
    : auction_status_message(false)
    , start_auction(false)
    , auction_finished(false)
    , occupied_ids()
    , requested_clusters()
    , auction_id(0)
    , robot_name()
    , available_clusters()  {
    }
  ExpAuction_(const ContainerAllocator& _alloc)
    : auction_status_message(false)
    , start_auction(false)
    , auction_finished(false)
    , occupied_ids(_alloc)
    , requested_clusters(_alloc)
    , auction_id(0)
    , robot_name(_alloc)
    , available_clusters(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _auction_status_message_type;
  _auction_status_message_type auction_status_message;

   typedef uint8_t _start_auction_type;
  _start_auction_type start_auction;

   typedef uint8_t _auction_finished_type;
  _auction_finished_type auction_finished;

   typedef std::vector< ::adhoc_communication::ExpAuctionElement_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::adhoc_communication::ExpAuctionElement_<ContainerAllocator> >::other >  _occupied_ids_type;
  _occupied_ids_type occupied_ids;

   typedef std::vector< ::adhoc_communication::ExpCluster_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::adhoc_communication::ExpCluster_<ContainerAllocator> >::other >  _requested_clusters_type;
  _requested_clusters_type requested_clusters;

   typedef uint32_t _auction_id_type;
  _auction_id_type auction_id;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _robot_name_type;
  _robot_name_type robot_name;

   typedef std::vector< ::adhoc_communication::ExpCluster_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::adhoc_communication::ExpCluster_<ContainerAllocator> >::other >  _available_clusters_type;
  _available_clusters_type available_clusters;




  typedef boost::shared_ptr< ::adhoc_communication::ExpAuction_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::adhoc_communication::ExpAuction_<ContainerAllocator> const> ConstPtr;

}; // struct ExpAuction_

typedef ::adhoc_communication::ExpAuction_<std::allocator<void> > ExpAuction;

typedef boost::shared_ptr< ::adhoc_communication::ExpAuction > ExpAuctionPtr;
typedef boost::shared_ptr< ::adhoc_communication::ExpAuction const> ExpAuctionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::adhoc_communication::ExpAuction_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::adhoc_communication::ExpAuction_<ContainerAllocator> >::stream(s, "", v);
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
struct IsFixedSize< ::adhoc_communication::ExpAuction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::adhoc_communication::ExpAuction_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::ExpAuction_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::adhoc_communication::ExpAuction_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::ExpAuction_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::adhoc_communication::ExpAuction_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::adhoc_communication::ExpAuction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "99f1253490d52d5e7eb6095beeea2711";
  }

  static const char* value(const ::adhoc_communication::ExpAuction_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x99f1253490d52d5eULL;
  static const uint64_t static_value2 = 0x7eb6095beeea2711ULL;
};

template<class ContainerAllocator>
struct DataType< ::adhoc_communication::ExpAuction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "adhoc_communication/ExpAuction";
  }

  static const char* value(const ::adhoc_communication::ExpAuction_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::adhoc_communication::ExpAuction_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool auction_status_message\n\
bool start_auction\n\
bool auction_finished\n\
ExpAuctionElement[] occupied_ids\n\
ExpCluster[] requested_clusters\n\
uint32 auction_id\n\
string robot_name\n\
ExpCluster[] available_clusters\n\
\n\
================================================================================\n\
MSG: adhoc_communication/ExpAuctionElement\n\
int64 id\n\
string detected_by_robot_str\n\
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

  static const char* value(const ::adhoc_communication::ExpAuction_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::adhoc_communication::ExpAuction_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.auction_status_message);
      stream.next(m.start_auction);
      stream.next(m.auction_finished);
      stream.next(m.occupied_ids);
      stream.next(m.requested_clusters);
      stream.next(m.auction_id);
      stream.next(m.robot_name);
      stream.next(m.available_clusters);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ExpAuction_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::adhoc_communication::ExpAuction_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::adhoc_communication::ExpAuction_<ContainerAllocator>& v)
  {
    s << indent << "auction_status_message: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.auction_status_message);
    s << indent << "start_auction: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.start_auction);
    s << indent << "auction_finished: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.auction_finished);
    s << indent << "occupied_ids[]" << std::endl;
    for (size_t i = 0; i < v.occupied_ids.size(); ++i)
    {
      s << indent << "  occupied_ids[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::adhoc_communication::ExpAuctionElement_<ContainerAllocator> >::stream(s, indent + "    ", v.occupied_ids[i]);
    }
    s << indent << "requested_clusters[]" << std::endl;
    for (size_t i = 0; i < v.requested_clusters.size(); ++i)
    {
      s << indent << "  requested_clusters[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::adhoc_communication::ExpCluster_<ContainerAllocator> >::stream(s, indent + "    ", v.requested_clusters[i]);
    }
    s << indent << "auction_id: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.auction_id);
    s << indent << "robot_name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.robot_name);
    s << indent << "available_clusters[]" << std::endl;
    for (size_t i = 0; i < v.available_clusters.size(); ++i)
    {
      s << indent << "  available_clusters[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::adhoc_communication::ExpCluster_<ContainerAllocator> >::stream(s, indent + "    ", v.available_clusters[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ADHOC_COMMUNICATION_MESSAGE_EXPAUCTION_H