import './TravelForm.css';
import { useState } from "react";

const TravelForm = () => {
    const [selectedActivities, setSelectedActivities] = useState([]);

    const activities = ['Architecture', 'Art', 'Beach', 'Hiking', 'History', 'Night-life', 'Shopping'];

    const handleCheckboxChange = (activity) => {
        setSelectedActivities((prevSelected) =>
          prevSelected.includes(activity)
            ? prevSelected.filter((item) => item !== activity) // Deselect if already selected
            : [...prevSelected, activity] // Select if not already selected
        );
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        console.log(selectedActivities);
    }

    return(
        <div className='formContainer'>
            <form className='form' onSubmit={handleSubmit}>
                <label htmlFor="location">Location</label>
                <input id="location"></input>
                <label htmlFor="budget">Budget</label>
                <input id="budget"></input>
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