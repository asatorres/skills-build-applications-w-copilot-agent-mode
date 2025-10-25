
import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    console.log('Workouts: Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results);
        console.log('Workouts: Fetched data:', results);
        setLoading(false);
      })
      .catch(err => {
        console.error('Workouts: Error fetching:', err);
        setLoading(false);
      });
  }, [endpoint]);

  if (loading) return (
    <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '200px' }}>
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading workouts...</span>
      </div>
    </div>
  );

  return (
    <div className="row justify-content-center">
      <div className="col-lg-10">
        <div className="card shadow mb-4">
          <div className="card-header bg-primary text-white d-flex align-items-center">
            <h2 className="mb-0 flex-grow-1"><i className="bi bi-heart-pulse-fill me-2"></i>Workouts</h2>
            <button className="btn btn-light btn-sm" onClick={() => window.location.reload()}>
              <i className="bi bi-arrow-clockwise"></i> Refresh
            </button>
          </div>
          <div className="card-body">
            <div className="table-responsive">
              <table className="table table-striped table-bordered align-middle">
                <thead className="table-primary">
                  <tr>
                    {workouts.length > 0 && Object.keys(workouts[0]).map((key) => (
                      <th key={key} className="text-capitalize">{key.replace(/_/g, ' ')}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {workouts.map((workout, idx) => (
                    <tr key={workout.id || idx}>
                      {Object.values(workout).map((val, i) => (
                        <td key={i}>{typeof val === 'object' ? JSON.stringify(val) : val}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            {workouts.length === 0 && (
              <div className="alert alert-info text-center mt-3">No workouts data available.</div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
