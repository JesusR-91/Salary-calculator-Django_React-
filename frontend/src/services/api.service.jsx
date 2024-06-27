import axios from "axios";

const getSalary = (salary) => {
    return axios.post('http://localhost:8000/netSalary', salary)
};

const getPayroll = (payroll) => {
    return axios.post('http://localhost:8000/payroll', payroll)
};

export {getSalary, getPayroll}