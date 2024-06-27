import React, { useEffect, useState } from 'react'
import { Button, Card, Form, Modal, Spinner } from 'react-bootstrap';
import { getSalary } from '../services/api.service';

export default function Salary() {
    const [community, setCommunity] = useState();
    const [salary, setSalary] = useState(0);
    const [result, setResult] = useState();
    const [reload, setReload] = useState(true);
    const [show, setShow] = useState(false);

    const handleCommunity = (event) =>{
        setCommunity(event.target.value);
    }
    
    const handleSalary = (event) =>{
        setSalary(event.target.value);
    }

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const getData = async (event) =>{
      event.preventDefault();
      const info = {'salary_base': salary, 'community' : community};
      try {
        setReload(false);
        const response = await getSalary(info);
        const salary = response.data;
        setResult(salary);
        setSalary(0);
        setCommunity("");
        setReload(true);
        handleShow();

      } catch (error) {
        console.log(error);
      }
    }

    useEffect(() => {}, [result])

    return (
      <div>
        {!reload ? (<Spinner animation="grow" />) :
        (<Form className='form'>
          <Form.Group className="mb-3 container">
            <Form.Label>Yearly gross salary </Form.Label>
            <Form.Control type="number" name='salary_base' value={salary} onChange={handleSalary}/>
          </Form.Group>

          <Form.Group className="mb-3 container">
            <Form.Label>Community</Form.Label>
            <Form.Select name='community' onChange={handleCommunity}>
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
          <Button variant="warning" type="submit" onClick={getData}>
            Submit
          </Button>
        </Form>)
        }
        {result ? (
          <Modal show={show} onHide={handleClose} className='modal-lg'>
            <Modal.Header closeButton>
              <Modal.Title>NET SALARY</Modal.Title>
            </Modal.Header>
            <Modal.Body className='payrollBox'>
              <h3>{result["net_salary"].toFixed(2)}</h3>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="warning" onClick={handleClose}>
                  Close
                </Button>
            </Modal.Footer>
          </Modal>
        ): ""}
      </div>
    )
}
