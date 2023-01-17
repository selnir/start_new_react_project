import { HashRouter, Routes, Route } from "react-router-dom";
import Main from "../pages/main";
import NoPage from "../pages/Nopage";
import App from "../App";

const Routeportefolio=
<HashRouter key="RouterPortefolio">
        <Routes >
          <Route path="/" element={<App />}>
            <Route index element={<Main />} />
            <Route path="*" element={<NoPage />} />
          </Route>
        </Routes>
</HashRouter>  

export default [Routeportefolio];