
import React, { useEffect, useState } from 'react';

const Teams = () => {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/teams/`;

  useEffect(() => {
    console.log('Teams: Fetching from:', endpoint);
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setTeams(results);
        console.log('Teams: Fetched data:', results);
        setLoading(false);
      })
      .catch(err => {
        console.error('Teams: Error fetching:', err);
        setLoading(false);
      });
  }, [endpoint]);

  if (loading) return (
    <div className="d-flex justify-content-center align-items-center" style={{ minHeight: '200px' }}>
      <div className="spinner-border text-primary" role="status">
        <span className="visually-hidden">Loading teams...</span>
      </div>
    </div>
  );

  return (
    <div className="row justify-content-center">
      <div className="col-lg-10">
        <div className="card shadow mb-4">
          <div className="card-header bg-primary text-white d-flex align-items-center">
            <h2 className="mb-0 flex-grow-1"><i className="bi bi-people-fill me-2"></i>Teams</h2>
            <button className="btn btn-light btn-sm" onClick={() => window.location.reload()}>
              <i className="bi bi-arrow-clockwise"></i> Refresh
            </button>
          </div>
          <div className="card-body">
            <div className="table-responsive">
              <table className="table table-striped table-bordered align-middle">
                <thead className="table-primary">
                  <tr>
                    {teams.length > 0 && Object.keys(teams[0]).map((key) => (
                      <th key={key} className="text-capitalize">{key.replace(/_/g, ' ')}</th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {teams.map((team, idx) => (
                    <tr key={team.id || idx}>
                      {Object.values(team).map((val, i) => (
                        <td key={i}>{typeof val === 'object' ? JSON.stringify(val) : val}</td>
                      ))}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            {teams.length === 0 && (
              <div className="alert alert-info text-center mt-3">No teams data available.</div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Teams;
