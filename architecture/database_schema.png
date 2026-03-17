create table users (
  id uuid primary key default gen_random_uuid(),
  full_name text not null,
  email text unique not null,
  phone text,
  role text default 'user',
  created_at timestamptz default now()
);

create table safety_circle_contacts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id) on delete cascade,
  contact_name text not null,
  contact_phone text,
  contact_email text,
  relationship text,
  created_at timestamptz default now()
);

create table panic_alerts (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id) on delete cascade,
  latitude numeric(9,6) not null,
  longitude numeric(9,6) not null,
  message text default 'Emergency alert triggered',
  status text default 'sent',
  created_at timestamptz default now()
);

create table location_sessions (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id) on delete cascade,
  start_latitude numeric(9,6),
  start_longitude numeric(9,6),
  is_active boolean default true,
  expires_at timestamptz,
  created_at timestamptz default now()
);

create table safety_checkins (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id) on delete cascade,
  status text not null,
  notes text,
  created_at timestamptz default now()
);
