import React, { useEffect, useState } from 'react'
import { Button, Card, Form, ListGroup, Modal } from 'react-bootstrap'
import { getPayroll } from '../services/api.service';

export default function Payroll() {
    const [formData, setFormData] = useState({
        salary: 0,
        extraHours: 0,
        sicknessDays: 0,
        community: "",
        proRateExtraPayments: 0,
        extraPayments: 0,
        complements: {},
    });

    const [reload, setReload] = useState(true);
    const [complementName, setComplementName] = useState("");
    const [complementValue, setComplementValue] = useState(0);
    const [payroll, setPayroll] = useState();
    const [show, setShow] = useState(false);


    const handleInputChange = (event, field) => {
        setFormData({
            ...formData,
            [field]: event.target.value
        });
    };

    const handleComplementName = (event) =>{
        setComplementName(event.target.value);
    };

    const handleComplementValue = (event) =>{
        setComplementValue(event.target.value);
    };

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const addComplement = (event, name, value) =>{
        event.preventDefault();
        setReload(false);
        setFormData(({...formData,["complements"] :{...formData.complements, [name] : parseInt(value)}}));
        setComplementName("");
        setComplementValue(0);
        setReload(true);
    };

    const getData = async (event) =>{
        event.preventDefault();
        try {
            setReload(false);
            const info = {
                'salary_base': formData.salary,
                'community': formData.community,
            }

            //Conditional information
            if(formData.complements){
                info['complements'] = formData.complements
            }

            if(formData.proRateExtraPayments){
                info['pro_rate_extra_payments'] = parseInt(formData.proRateExtraPayments);
            }

            if(formData.extraPayments){
                info['extra_payments'] = parseInt(formData.extraPayments);
            }

            if(formData.extraHours){
                info['extra_hours'] = parseInt(formData.extraHours);
            }

            if(formData.sicknessDays){
                info['sickness_day'] = parseInt(formData.sicknessDays);
            }
            
            const response = await getPayroll(info);
            const data = response.data;
            setPayroll(data);
            handleShow();

            //Resetting the form data
            setFormData({
                salary: 0,
                extraHours: 0,
                sicknessDays: 0,
                community: "",
                proRateExtraPayments: 0,
                extraPayments: 0,
                complements: {},
            })

            setReload(true);           
        } catch (error) {
            console.log(error);            
        }
    }

    useEffect(() =>{
    }, [])


  return (
    <div>
        {!reload ? (<h2>Loading</h2>) : 
          (
              <Form className='App'>
                  <Form.Group className='container form-inline'>
                      <Form.Label className="mr-2"><strong>Base salary</strong></Form.Label>
                      <Form.Control type="number" name='salary_base' value={formData.salary} onChange={(e) => handleInputChange(e, 'salary')}/>
                  </Form.Group>
          
                  <Form.Group className="mb-3 container">
                      <Form.Label> <strong>Community</strong></Form.Label>
                      <Form.Select name='community' onChange={(e) => handleInputChange(e, 'community')}>
                          <option>Select community</option>
                          <option>Andalucía</option>
                          <option>Aragón</option>
                          <option>Asturias</option>
                          <option>Baleares</option>
                          <option>Canarias</option>
                          <option>Cantabria</option>
                          <option>Castilla la Mancha</option>
                          <option>Castilla y León</option>
                          <option>Cataluña</option>
                          <option>Comunidad de Madrid</option>
                          <option>Comunidad Valenciana</option>
                          <option>Extremadura</option>
                          <option>Galicia</option>
                          <option>La Rioja</option>
                          <option>Murcia</option>
                          <option>Navarra</option>
                          <option>País Vasco</option>
                      </Form.Select>
                  </Form.Group>
          
                  <Form.Group className='container'>
                      <Form.Label> <strong>Extra hours</strong></Form.Label>
                      <Form.Control type="number" name='extraHours' value={formData.extraHours} onChange={(e) => handleInputChange(e, 'extraHours')}/>
                  </Form.Group>
          
                  <Form.Group className='container'>
                      <Form.Label> <strong>Sickness days</strong></Form.Label>
                      <Form.Control type="number" name='sicknessDays' value={formData.sicknessDays} onChange={(e) => handleInputChange(e, 'sicknessDays')}/>
                  </Form.Group>

                  <Form.Group className='container'>
                      <Form.Label> <strong>Pro rate extra payments</strong></Form.Label>
                      <Form.Control type="number" name='proRateExtraPayments' value={formData.proRateExtraPayments} onChange={(e) => handleInputChange(e, 'proRateExtraPayments')}/>
                  </Form.Group>

                  <Form.Group className='container'>
                      <Form.Label> <strong>Extra payments</strong></Form.Label>
                      <Form.Control type="number" name='extraPayments' value={formData.extraPayments} onChange={(e) => handleInputChange(e, 'extraPayments')}/>
                  </Form.Group>      

                  <Form.Group className='container'>
                      <Form.Label><strong>Complements: </strong></Form.Label>
                      {Object.keys(formData.complements).length > 0 ? Object.keys(formData.complements).map(key => (
                          <li>
                              {key}: {formData.complements[key]}
                          </li>
                      )) : <p>No complements added</p>}

                      <hr />

                      <Form.Label>Add new complements: </Form.Label>
          
                      <div style={{display: 'flex', justifyContent: 'center' , gap: '5%'}}>
                          <input type="text" placeholder="Name of the complement" value={complementName} onChange={handleComplementName}/>
                          <input type="number" value={complementValue} onChange={handleComplementValue}/>
                          <button onClick={(event) => addComplement(event, complementName, complementValue)}>Add</button>
                      </div>
                  </Form.Group>
          
                  <br />
                  <Button variant="warning" type="submit" onClick={getData}>
                      Submit
                  </Button>
              </Form>
            )
            
        }

        {payroll ? 
        <Modal show={show} onHide={handleClose} className='modal-lg'>
            <Modal.Header closeButton>
                <Modal.Title>PAYROLL</Modal.Title>
            </Modal.Header>
            <Modal.Body className='payrollBox'>
                <Card className='payrollCard'>
                    <h5>Employee information</h5>
                    <hr/>
                    <ul>Base salary: {payroll.employee['Base salary'].toFixed(2)}</ul>

                    {payroll.employee['Pro-rate extra payment'] ? <ul>Prorated extra payment:  {payroll.employee['Pro-rate extra payment'].toFixed(2)} </ul> : ""}

                    {payroll.employee['Extra payment'] ? <ul>Extra payment:  {payroll.employee['Extra payment'].toFixed(2)} </ul> : ""}
                    
                    <ul>Complements: 
                        {Object.keys(payroll.employee['Complements']) > 0 ? Object.keys(payroll.employee['Complements']).map((key) =>(
                        <ul>
                            {key}: {payroll.employee['Complements'][key]}
                        </ul>
                        )) : (<ul>None</ul>)}
                    </ul>
                    <ul>Irpf: {payroll.employee['Irpf'].toFixed(2)}</ul>
                    <ul>Social security deductions: 
                        {Object.keys(payroll.employee['social security deductions']) ? Object.keys(payroll.employee['social security deductions']).map((key) =>(
                        <ul>
                            {key}: {payroll.employee['social security deductions'][key].toFixed(2)}
                        </ul>
                        )) : (<ul>None</ul>)}
                    </ul>
                    <ul>Net salary: {payroll.employee['Net salary'].toFixed(2)}</ul>
                </Card>
                <Card  className='payrollCard'>
                    <h5>Company Information</h5>
                    <hr/>
                    <ul>Common contingencies company: {payroll.company['Common contingencies company'].toFixed(2)}</ul>
                    <ul>At ep: {payroll.company['At ep'].toFixed(2)}</ul>
                    <ul>Unemployment: {payroll.company['Unemployment company'].toFixed(2)}</ul>
                    <ul>Professional training: {payroll.company['Professional training company'].toFixed(2)}</ul>
                    <ul>Fogasa: {payroll.company['Fogasa'].toFixed(2)}</ul>
                    <ul>Total company deductions: {payroll.company['Total company deductions'].toFixed(2)}</ul>
                </Card>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="warning" onClick={handleClose}>Close</Button>
            </Modal.Footer>
      </Modal>
      : ""}
    </div>)  
}
