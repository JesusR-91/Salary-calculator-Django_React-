import './App.css';
import { Route, Routes, useLocation } from 'react-router-dom';
import Salary from './components/Salary';
import Payroll from './components/Payroll';
import Home from './pages/Home';
import NavBar from './components/NavBar';


function App() {

  const location = useLocation();

  return (
    <div className='App'>
      <NavBar location={location}/>
      
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/salary' element={<Salary/>}/>
        <Route path='/payroll' element={<Payroll/>}/>
      </Routes>  
    </div>
  );
}

export default App;
