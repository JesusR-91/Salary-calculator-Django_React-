import React, { useEffect } from 'react'
import { Button } from 'react-bootstrap';

export default function NavBar({location}) {
  useEffect(() => {
  }, [location.pathname])

  return (
    <div className='navBar'>
        {location.pathname === "/" ? null : (<Button variant='dark' href='/'>Home</Button>)}
        {location.pathname === "/salary" || location.pathname === "/"? null : (<Button variant='warning' href='/salary'>Salary</Button>)}
        {location.pathname === "/payroll" || location.pathname === "/"? null : (<Button variant='warning' href='/payroll'>Payroll</Button>)}
    </div>
  )
}
