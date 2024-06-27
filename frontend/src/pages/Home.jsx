import React from 'react'
import { Button } from 'react-bootstrap'

export default function Home() {
  return (
    <div className='home'>
      <h2>What would you like to calculate?</h2>
      <hr />
      <div className='box'>
        <Button variant="warning" type="primary" href='/salary'>Salary</Button>
        <br />
        <Button variant="warning" type="primary" href='/payroll'>Payroll</Button>
      </div>
    </div>
  )
}
