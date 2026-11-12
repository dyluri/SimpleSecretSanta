This is a simple secret santa discord bot 🎄

Follows a very similar implementation to putting everyones name in a bag and drawing them out, which means every now and then the last person draws their own name and everyone has to start over :P

Create a .env with a discord bot token that has read write access, dont really remember all the steps of that to be honest, example .env provided

Type `!help` to see all the commands when running the bot

Add your own responses to certain messages to troll your friends

## Vercel hosting

Import the repository with the **Other** application preset and keep the root
directory at the repository root. Add `TOKEN` as a Production environment
variable in Vercel, not in Git. Enable Message Content Intent for the bot in
the Discord Developer Portal.

The Dockerfile and `vercel.json` run one `santa` daemon with 1 GiB of memory.
The `public` directory contains a placeholder page because Vercel requires
nonempty static output. It does not report bot health.
Daemons run only on production deployments.
After deploying, check **Daemons** and the runtime logs for the bot's
`is now running` message.

Hobby currently includes 420 GB-hours of daemon memory per month, shared
across the team, plus 5 active CPU-hours. One 1 GiB instance can run for about
17.5 days before exhausting the memory quota if no other daemons use it.
Stop the daemon by setting its instance count to zero when it is not needed.
See https://vercel.com/docs/daemons/limits for current quotas.

Enrollment and drawing state are held in memory. Restarts and deployments
reset them, and `!save_names` writes only to the container's temporary local
filesystem. Do not rely on it surviving a restart; durable storage is not
configured.
