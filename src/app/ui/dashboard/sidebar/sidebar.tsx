import React from 'react'
import Image from 'next/image';

import '../dashboardui.css'
import '../sidebar/sidebar.css'
import HomeIcon from '@mui/icons-material/Home';
import MapsHomeWorkIcon from '@mui/icons-material/MapsHomeWork';
import BuildIcon from '@mui/icons-material/Build';
import SchoolIcon from '@mui/icons-material/School';
import PersonIcon from '@mui/icons-material/Person';
import LocalLibraryIcon from '@mui/icons-material/LocalLibrary';
import ForumIcon from '@mui/icons-material/Forum';
import AddIcon from '@mui/icons-material/Add';
import NotificationsActiveIcon from '@mui/icons-material/NotificationsActive';
import LogoutIcon from '@mui/icons-material/Logout';
import Link from 'next/link';
import Logo from '../../../../../public/dbu.png'
const Menuitems = {
  title:"name",
  list:[{
    id:1,
    title:"Campus",
    path:"/dashboard/campus",
    icon:<BuildIcon/>},
  {
    id:1,
  title:"Collage",
  path:"/dashboard/collage",
  icon:<MapsHomeWorkIcon/>},
  {
    title:"Department",
    path:"/dashboard/departments",
    icon:<SchoolIcon/>

}
,
  { id:1,
    title:"Follow",
    path:"/dashboard/follow",
    icon:<PersonIcon/>

},
{
  id:2,
  title:"Lectures",
  path:"/dashboard/lectures",
  icon:<LocalLibraryIcon/>

},
{
  id:2,
  title:"Messages",
  path:"/dashboard/messages",
  icon:<ForumIcon/>

},
{
  id:2,
  title:"News",
  path:"/dashboard/news",
  icon:<AddIcon/>

},
{
  id:3,
  title:"Notifications",
  path:"/dashboard/notfcations",
  icon:<NotificationsActiveIcon/>

},
{
  id:3,
  title:"Collage",
  path:"/dashboard/collage",
  icon:<MapsHomeWorkIcon/>

},
{
  id:3,
  title:"Logout",
  path:"/dashboard/logout",
  icon:<LogoutIcon/>

}]
  
}
export default function sidebar() {
  return (

    <div className='sidebarcontainer' ><span className='name'>Debre Birhan</span> 
<Image src={Logo} alt='logo' width={100} height={100} objectFit='cover' style={{borderRadius:"50%"}}/>
    <ul>
    {Menuitems.list.map((item)=>
      (
        <li key={item.title}>
         
          <Link href={item.path}> {item.icon}{item.title}
          
          </Link>
         <div className='line'>

           </div>
        
         
        </li>
      ))}
    </ul>
    </div>
  )
}
