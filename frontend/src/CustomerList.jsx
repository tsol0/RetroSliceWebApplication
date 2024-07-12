import React from "react"

const CustomerList = ({ customers, updateCustomer, updateCallback}) => {
    return (
        <div>
            <h2>Customers</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Age</th>
                        <th>Employed Status</th>
                        <th>Email</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {customers.map((customer) => (
                        <tr key={customer.id}>
                            <td>{customer.name}</td>
                            <td>{customer.age}</td>
                            <td>{customer.employed}</td>
                            <td>{customer.email}</td>
                            {/* <td>
                                <button onClick={""}>Update</button>
                                <button onClick={""}>Delete</button>
                            </td> */}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}

export default CustomerList