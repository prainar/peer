import { createBrowserRouter } from 'react-router-dom';
import Login from '../components/auth/Login';
import Signup from '../components/auth/Signup';
import ProfileView from '../components/profile/ProfileView';
import ProfileEdit from '../components/profile/ProfileEdit';
import PostCreate from '../components/posts/PostCreate';
import PostList from '../components/posts/PostList';
// import Feed from '../components/feed/Feed'; // Unused import
import JobList from '../components/job-board/JobList';
import MessageList from '../components/messaging/MessageList';
import Dashboard from '../components/dashboard/Dashboard';
import ThreeDemo from '../components/ThreeDemo';
import RouteTest from '../components/RouteTest';

// Debug function to log route changes
const debugRoute = (path: string) => {
  console.log('🔗 Route accessed:', path);
  return true;
};

export const router = createBrowserRouter([
  {
    path: '/',
    element: <Login />,
    loader: () => debugRoute('/'),
  },
  {
    path: '/login',
    element: <Login />,
    loader: () => debugRoute('/login'),
  },
  {
    path: '/signup',
    element: <Signup />,
    loader: () => debugRoute('/signup'),
  },
  {
    path: '/dashboard',
    element: <Dashboard />,
  },
  {
    path: '/profile',
    element: <ProfileView />,
  },
  {
    path: '/profile/edit',
    element: <ProfileEdit />,
  },
  {
    path: '/posts/create',
    element: <PostCreate />,
  },
  {
    path: '/posts',
    element: <PostList />,
  },
  {
    path: '/jobs',
    element: <JobList />,
  },
  {
    path: '/messages',
    element: <MessageList />,
  },
  {
    path: '/three-demo',
    element: <ThreeDemo />,
  },
  {
    path: '/test-route',
    element: <RouteTest />,
    loader: () => debugRoute('/test-route'),
  },
]); 