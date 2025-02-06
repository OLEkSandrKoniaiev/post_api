import {Outlet} from "react-router-dom";
import {NavComponent} from '../components/navigation/NavComponent.tsx';

export const MainLayout = () => {
    return (
        <div className="mx-auto">
            <NavComponent/>
            <Outlet/>
        </div>
    );
};
