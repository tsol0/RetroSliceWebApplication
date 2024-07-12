import {useState} from "react"

const Customer = ({ existingCustomer = {}, updateCallback}) => {
    const [name, setName] = useState(existingCustomer.name || "")
    const [age, setAge] = useState(existingCustomer.age || "")
    const [arcadeScore, setArcadeScore] = useState(existingCustomer.arcadeScore || "")
    const [bowlingScore, setBowlingScore] = useState(existingCustomer.bowlingScore || "")
    const [pizzasConsumed, setPizzasConsumed] = useState(existingCustomer.pizzasConsumed || "")
    const [slushyPreference, setSlushyPreference] = useState(existingCustomer.slushyPreference || "")
    const [slushiesConsumed, setSlushiesConsumed] = useState(existingCustomer.slushiesConsumed || "")
    const [employed, setEmployed] = useState(existingCustomer.employed || "")
    const [email, setEmail] = useState(existingCustomer.email || "")

    const updating = Object.entries(existingCustomer).length !== 0

    const onSubmit = async (e) => {

        const data = {
            name,
            age,
            arcadeScore ,
            bowlingScore ,
            pizzasConsumed ,
            slushyPreference,
            slushiesConsumed ,
            employed,
            email
        }

        const url = "http://127.0.0.1:5000/" + (updating ? `update_contact/${existingCustomer.name}` : `create_contact`) 
        
        const response = await fetch(url, options)

    }
}