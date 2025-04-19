import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch('https://ubiquitous-space-chainsaw-9g699p97gr3xxxp-8000.app.github.dev/api/activities')
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center mb-4">Activities</h1>
      <div className="card">
        <div className="card-body">
          <table className="table table-striped table-bordered">
            <thead className="thead-dark">
              <tr>
                <th>#</th>
                <th>Activity Name</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity, index) => (
                <tr key={activity.id}>
                  <td>{index + 1}</td>
                  <td>{activity.name}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

export default Activities;