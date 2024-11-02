import { useState } from "react";

const TravelForm = () => {
    const [selectedActivities, setSelectedActivities] = useState([]);

    const activities = ['Art', 'Beach', 'Hiking', 'History', 'Night-life', 'Shopping'];

    const handleCheckboxChange = () => {

    }

    return(
        <div className='formContainer'>
            <form className='form'>
                <label for="location">Location</label><br/>
                <input id="location"></input>
                <label for="budget">Budget</label><br/>
                <input id="budget"></input>
            `   <div>
                    {activities.map(activity =>
                        <div key={activity}>
                            <label>
                                <input type="checkbox" value={activity} checked={selectedActivities.includes(activity)} onChange={handleCheckboxChange}/>
                                {activity}
                            </label>
                        </div>)
                    }
                </div>
                <button type='submit'>Submit</button>
            </form>
        </div>
    );
}

export default TravelForm;