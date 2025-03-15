/*

Project Root:

npx create-react-app frontend
cd frontend

Install Axios:

npm install axios

*/

// MAIN APP

import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./Login";
import Protected from "./Protected";

function App() {
  const isAuthenticated = localStorage.getItem("token");

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route
          path="/protected"
          element={isAuthenticated ? <Protected /> : <Navigate to="/" />}
        />
      </Routes>
    </Router>
  );
}

export default App;
