import './TravelForm.css';
import axios from 'axios';
import { useState } from "react";

const TravelForm = () => {
    const [location, setLocation] = useState('');
    const [budget, setBudget] = useState('');
    const [selectedActivities, setSelectedActivities] = useState([]);
    const [result, setResult] = useState(null);

    const activities = ['Architecture', 'Art', 'Beach', 'Hiking', 'History', 'Night-life', 'Shopping'];

    const handleCheckboxChange = (activity) => {
        setSelectedActivities((prevSelected) =>
          prevSelected.includes(activity)
            ? prevSelected.filter((item) => item !== activity) // Deselect if already selected
            : [...prevSelected, activity] // Select if not already selected
        );
    };

    const handleSubmit = async (event) => {
        event.preventDefault();

        const formData = {
            city: location,
            budget: budget,
            preferences: selectedActivities
        }

        try {
            const response = await axios.post('http://127.0.0.1:5000/process', formData, {headers: {"Content-Type": "application/json"}});
            setResult(response.data.result);
        } catch (err) {
            console.error(err);
        }
    }

    return(
        <div className='formContainer'>
            <form className='form' onSubmit={handleSubmit}>
                <label htmlFor="location">Location</label>
                <input value={location} onChange={(e) => setLocation(e.target.value)} id="location"></input>
                <label htmlFor="budget">Budget</label>
                <input value={budget} onChange={(e) => setBudget(e.target.value)}id="budget"></input>
                <label>Interests</label>
            `   <div className="activitiesContainer">
                    {activities.map(activity =>
                        <div key={activity} className={selectedActivities.includes(activity) ? "activity selected" : "activity"} onClick={() => handleCheckboxChange(activity)}>
                            {activity}
                        </div>
                    )}
                </div>
                <button type='submit'>Submit</button>
            </form>
        </div>
    );
}

export default TravelForm;