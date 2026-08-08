import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

export function middleware(request: NextRequest) {
  const accessToken = request.cookies.get('access_token')?.value;
  const refreshToken = request.cookies.get('refresh_token')?.value;
  
  const isAuthenticated = !!(accessToken || refreshToken);
  
  // Protect /dashboard routes
  if (request.nextUrl.pathname.startsWith('/dashboard')) {
    if (!isAuthenticated) {
      // Redirect unauthenticated users to the landing/login page
      return NextResponse.redirect(new URL('/', request.url));
    }
  }

  // Redirect authenticated users away from the landing/login page
  if (request.nextUrl.pathname === '/') {
    if (isAuthenticated) {
      return NextResponse.redirect(new URL('/dashboard', request.url));
    }
  }
  
  return NextResponse.next();
}

// Configure which routes the middleware runs on
export const config = {
  matcher: [
    /*
     * Match all request paths except for the ones starting with:
     * - api (API routes)
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    '/((?!api|_next/static|_next/image|favicon.ico).*)',
  ],
};