'use cleant'
import React from 'react'
import Sidebar from '../ui/dashboard/sidebar/sidebar'
import Navbar from '../ui/dashboard/navbar/navbar'
import '../ui/globals.css'
import '../ui/dashboard/dashboardui.css'
function layout({children}) {
  return (
    <div className='container'>

        <div className='sidebar'>
        <Sidebar/>
        </div>
        <div className='navbar'> 
         <Navbar/>

        </div>
<div>
    {children}
</div>


    </div>
  )
}

export default layout